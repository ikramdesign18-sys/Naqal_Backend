from fastapi import APIRouter, File, UploadFile, HTTPException, Form
from app.services.face_analyzer import FaceAnalyzer
from app.services.model_trainer import ModelTrainer
from app.services.supabase_client import supabase
from PIL import Image
import io
import uuid

router = APIRouter()
face_analyzer = FaceAnalyzer()
model_trainer = ModelTrainer()

@router.post("/scan")
async def scan_face(
    image: UploadFile = File(...),
    skin_tone: str = Form("medium"),
    gender: str = Form("unspecified"),
    region: str = Form("pakistan")
):
    try:
        # Read and validate image
        image_bytes = await image.read()
        
        # Verify it's a valid image
        try:
            img = Image.open(io.BytesIO(image_bytes))
            img.verify()
            # Re-open after verify
            image_bytes = io.BytesIO(image_bytes)
            image_bytes = image_bytes.getvalue()
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid image file: {str(e)}")
        
        # Analyze face
        results = await face_analyzer.analyze(image_bytes)
        
        # Save as training data with metadata
        metadata = {
            "skin_tone": skin_tone,
            "gender": gender,
            "region": region,
        }
        try:
            await model_trainer.save_training_sample(image_bytes, results, metadata)
        except:
            pass  # Training save is optional
        
        # Save to database
        scan_id = str(uuid.uuid4())
        try:
            supabase.table("face_scans").insert({
                "id": scan_id,
                "acne_score": results["acne_score"],
                "redness_score": results["redness_score"],
                "dark_circles_score": results["dark_circles_score"],
                "texture_score": results["texture_score"],
                "hydration_score": results["hydration_score"],
                "sensitivity_score": results["sensitivity_score"],
                "estimated_age": results["estimated_age"],
                "overall_health": results["overall_health"]
            }).execute()
        except:
            pass  # Database save is optional for testing
        
        return {
            "status": "success",
            "scan_id": scan_id,
            "data": results
        }
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")