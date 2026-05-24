import cv2
import mediapipe as mp
import numpy as np
from PIL import Image
import io
import os
import json

# Load Naqal AI Ultimate model (predicts all 6 skin metrics + age)
naqal_model = None

try:
    from tensorflow.keras.models import load_model
    
    # Load Ultimate: Trained on 7,572 labeled images from 3 datasets
    ultimate_path = os.path.join(os.path.dirname(__file__), '..', '..', 'ml', 'models', 'naqal_ultimate.h5')
    if os.path.exists(ultimate_path):
        naqal_model = load_model(ultimate_path)
        print("✅ Naqal AI Ultimate loaded (7,572 labeled skin images)")
        
except Exception as e:
    print(f"⚠️ Model loading error: {e}")

# Try to load Groq service
groq_service = None
try:
    from app.services.groq_service import analyze_face_with_ai
    groq_service = analyze_face_with_ai
    print("✅ Groq AI Vision service loaded")
except Exception as e:
    print(f"⚠️ Groq service not loaded: {e}")

# Try to load HuggingFace service
hf_tone_analyzer = None
hf_recommendations = None
try:
    from app.services.huggingface_service import analyze_skin_tone, get_skincare_recommendations
    hf_tone_analyzer = analyze_skin_tone
    hf_recommendations = get_skincare_recommendations
    print("✅ HuggingFace Skin Analysis service loaded")
except Exception as e:
    print(f"⚠️ HuggingFace service not loaded: {e}")

class FaceAnalyzer:
    """
    Naqal AI Face Analysis Engine ULTIMATE + Groq AI + HuggingFace
    Hybrid: Naqal Ultimate Model + Groq LLaMA 3.1 + HuggingFace Models
    MediaPipe 478-point mesh for face detection
    Predicts ALL 6 skin metrics directly
    """
    
    def __init__(self):
        self.mp_face = mp.solutions.face_mesh.FaceMesh(
            static_image_mode=True,
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5
        )
        self.use_ai = naqal_model is not None
        self.use_groq = groq_service is not None
        self.use_hf = hf_tone_analyzer is not None
        self.regions = {
            "forehead": [10, 67, 69, 109, 151, 337, 299, 333],
            "left_cheek": [50, 118, 101, 36, 143, 123, 116, 142],
            "right_cheek": [280, 347, 330, 266, 372, 352, 345, 371],
            "nose": [1, 2, 4, 5, 6, 19, 45, 51],
            "under_eye_left": [33, 133, 155, 157, 158, 159, 160, 161, 173],
            "under_eye_right": [362, 263, 387, 386, 385, 384, 398, 382, 381],
        }
    
    async def analyze(self, image_bytes: bytes) -> dict:
        image = Image.open(io.BytesIO(image_bytes))
        image_np = np.array(image.convert('RGB'))
        h, w, _ = image_np.shape
        
        results = self.mp_face.process(image_np)
        
        if not results.multi_face_landmarks:
            raise ValueError("No face detected. Please try again with better lighting.")
        
        landmarks = results.multi_face_landmarks[0]
        regions = self._extract_regions(image_np, landmarks, h, w)
        
        # Prepare face for AI
        face_crop = cv2.resize(image_np, (224, 224))
        face_input = np.expand_dims(face_crop.astype(np.float32) / 255.0, axis=0)
        
        # AI prediction: Ultimate model predicts all metrics
        if self.use_ai:
            ai_pred = naqal_model.predict(face_input, verbose=0)[0]
            acne = round(ai_pred[0] * 100)
            redness = round(ai_pred[1] * 100)
            dark_circles = round(ai_pred[2] * 100)
            texture = round(ai_pred[3] * 100)
            hydration = round(ai_pred[4] * 100)
            sensitivity = round(ai_pred[5] * 100)
            engine = "naqal_ultimate"
        else:
            acne = self._analyze_acne(regions)
            redness = self._analyze_redness(regions)
            dark_circles = self._analyze_dark_circles(regions)
            texture = self._analyze_texture(regions)
            hydration = self._estimate_hydration(regions)
            sensitivity = self._estimate_sensitivity(regions)
            engine = "algorithmic_fallback"
        
        # Groq AI Vision enhancement (if available)
        groq_summary = None
        if self.use_groq:
            try:
                region_desc = f"Face with acne:{acne}, redness:{redness}, dark_circles:{dark_circles}, texture:{texture}, hydration:{hydration}"
                groq_result = groq_service(region_desc)
                
                if groq_result and isinstance(groq_result, dict):
                    if all(k in groq_result for k in ['acne_score', 'redness_score', 'dark_circles_score', 'texture_score', 'hydration_score', 'sensitivity_score']):
                        acne = round(acne * 0.7 + float(groq_result['acne_score']) * 0.3)
                        redness = round(redness * 0.7 + float(groq_result['redness_score']) * 0.3)
                        dark_circles = round(dark_circles * 0.7 + float(groq_result['dark_circles_score']) * 0.3)
                        texture = round(texture * 0.7 + float(groq_result['texture_score']) * 0.3)
                        hydration = round(hydration * 0.7 + float(groq_result['hydration_score']) * 0.3)
                        sensitivity = round(sensitivity * 0.7 + float(groq_result['sensitivity_score']) * 0.3)
                        engine = "naqal_ultimate_groq"
                    
                    if 'summary' in groq_result:
                        groq_summary = groq_result['summary']
                        
                    if 'estimated_age' in groq_result:
                        estimated_age = int(groq_result['estimated_age'])
            except Exception as e:
                print(f"Groq enhancement skipped: {e}")
        
                # Age: algorithmic default
        estimated_age = self._estimate_age(landmarks, h, w)
        
        overall = round((
            hydration + (100 - acne) + (100 - sensitivity) + 
            texture + (100 - redness) + (100 - dark_circles)
        ) / 6)
        
        result = {
            "acne_score": round(acne),
            "redness_score": round(redness),
            "dark_circles_score": round(dark_circles),
            "texture_score": round(texture),
            "hydration_score": round(hydration),
            "sensitivity_score": round(sensitivity),
            "estimated_age": estimated_age,
            "overall_health": overall,
            "engine": engine
        }
        
        # Add Groq AI summary if available
        if groq_summary:
            result["ai_summary"] = groq_summary
        
        # HuggingFace skin tone analysis (if available)
        if self.use_hf:
            try:
                hf_tone = hf_tone_analyzer(image_bytes)
                if hf_tone:
                    result["skin_tone"] = hf_tone
                
                # Get skincare recommendations based on detected skin type
                skin_type_for_recs = "oily" if acne > 50 else "dry" if hydration < 40 else "sensitive" if sensitivity > 60 else "combination"
                hf_recs = hf_recommendations(skin_type_for_recs, ["acne", "redness", "dark_circles"])
                if hf_recs:
                    result["recommendations"] = hf_recs
            except Exception as e:
                print(f"HuggingFace enhancement skipped: {e}")
        
        return result
    
    def _extract_regions(self, image, landmarks, h, w):
        regions = {}
        for name, ids in self.regions.items():
            points = []
            for idx in ids:
                lm = landmarks.landmark[idx]
                points.append([int(lm.x * w), int(lm.y * h)])
            points = np.array(points)
            x_min, y_min = np.min(points, axis=0)
            x_max, y_max = np.max(points, axis=0)
            pad = 10
            region = image[
                max(0, y_min-pad):min(h, y_max+pad),
                max(0, x_min-pad):min(w, x_max+pad)
            ]
            if region.size > 0:
                regions[name] = cv2.resize(region, (224, 224))
        return regions
    
    def _analyze_acne(self, regions) -> float:
        scores = []
        for name in ["forehead", "left_cheek", "right_cheek", "nose"]:
            if name in regions:
                region = regions[name]
                gray = cv2.cvtColor(region, cv2.COLOR_RGB2GRAY)
                variance = cv2.Laplacian(gray, cv2.CV_64F).var()
                _, thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)
                dark_ratio = np.sum(thresh > 0) / thresh.size
                scores.append(min(100, (variance / 5) + (dark_ratio * 200)))
        return np.mean(scores) if scores else 30
    
    def _analyze_redness(self, regions) -> float:
        scores = []
        for name in ["left_cheek", "right_cheek", "nose"]:
            if name in regions:
                region = regions[name]
                r, g, b = region[:,:,0].astype(float), region[:,:,1].astype(float), region[:,:,2].astype(float)
                redness_index = np.mean(r / (g + b + 1))
                scores.append(min(100, max(0, (redness_index - 1.0) * 150)))
        return np.mean(scores) if scores else 20
    
    def _analyze_dark_circles(self, regions) -> float:
        scores = []
        for name in ["under_eye_left", "under_eye_right"]:
            if name in regions:
                region = regions[name]
                lab = cv2.cvtColor(region, cv2.COLOR_RGB2LAB)
                l_channel = lab[:, :, 0]
                darkness = 100 - np.mean(l_channel)
                scores.append(min(100, max(0, darkness * 1.5)))
        return np.mean(scores) if scores else 30
    
    def _analyze_texture(self, regions) -> float:
        scores = []
        for name in ["left_cheek", "right_cheek", "forehead"]:
            if name in regions:
                region = regions[name]
                gray = cv2.cvtColor(region, cv2.COLOR_RGB2GRAY)
                variance = cv2.Laplacian(gray, cv2.CV_64F).var()
                scores.append(max(0, 100 - (variance / 8)))
        return np.mean(scores) if scores else 50
    
    def _estimate_hydration(self, regions) -> float:
        scores = []
        for name in ["forehead", "left_cheek"]:
            if name in regions:
                region = regions[name]
                gray = cv2.cvtColor(region, cv2.COLOR_RGB2GRAY)
                brightness = np.mean(gray)
                variance = np.var(gray)
                scores.append(min(100, max(0, (brightness * 0.5) + ((255 - variance) * 0.5))))
        return np.mean(scores) if scores else 50
    
    def _estimate_sensitivity(self, regions) -> float:
        if "left_cheek" in regions and "right_cheek" in regions:
            left = self._analyze_redness({"left_cheek": regions["left_cheek"]})
            right = self._analyze_redness({"right_cheek": regions["right_cheek"]})
            variance = abs(left - right)
            return min(100, 30 + (variance * 2))
        return 40
    
    def _estimate_age(self, landmarks, h, w) -> int:
        left_fold = abs(landmarks.landmark[50].y - landmarks.landmark[118].y)
        right_fold = abs(landmarks.landmark[280].y - landmarks.landmark[347].y)
        fold_depth = (left_fold + right_fold) / 2
        eye_level = (landmarks.landmark[33].y + landmarks.landmark[263].y) / 2
        jaw_width = abs(landmarks.landmark[172].x - landmarks.landmark[397].x)
        age = 22 + (fold_depth * 200) + (eye_level * 30) - (jaw_width * 15)
        return max(16, min(70, int(age)))