"""
Naqal Data Processing Pipeline
Processes all datasets into unified training format
Memory-efficient batch processing
"""

import os
import json
import numpy as np
from PIL import Image
from datasets import load_from_disk

class DataProcessor:
    def __init__(self):
        self.base_path = os.path.join(os.path.dirname(__file__), '..', '..', 'datasets')
        self.output_path = os.path.join(os.path.dirname(__file__), '..', '..', 'processed_data')
        os.makedirs(self.output_path, exist_ok=True)
    
    def process_fairface(self):
        """Extract faces from FairFace - saves directly to disk"""
        print("Processing FairFace...")
        dataset = load_from_disk(os.path.join(self.base_path, 'fairface'))
        
        saved_count = 0
        save_data = []
        
        for i, item in enumerate(dataset):
            img_filename = f"fairface_{i:06d}.jpg"
            img_path = os.path.join(self.output_path, img_filename)
            
            try:
                item['image'].resize((224, 224)).save(img_path, 'JPEG', quality=85)
            except:
                continue
            
            save_data.append({
                'image_path': img_filename,
                'age': item['age'],
                'gender': item['gender'],
                'race': item['race'],
                'acne': 0,
                'acne_marks': 0,
                'stains': 0,
                'wrinkles': 0,
                'dark_circles': 0,
                'source': 'fairface'
            })
            saved_count += 1
            
            if saved_count % 5000 == 0:
                print(f"  FairFace: {saved_count}/{len(dataset)} images saved")
        
        print(f"FairFace processed: {saved_count} images")
        return save_data
    
    def process_4788_defects(self):
        """Process 4788 skin defects with labels from filenames"""
        print("Processing 4788 Skin Defects...")
        
        defects_path = os.path.join(
            self.base_path, 
            'GlowMix', 
            '4788-images-Human-Facial-Skin-Defects-Data-main',
            '4788-images-Human-Facial-Skin-Defects-Data-main'
        )
        
        save_data = []
        
        all_files = [f for f in os.listdir(defects_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
        print(f"  Found {len(all_files)} image files")
        
        for idx, filename in enumerate(all_files):
            name = filename.replace('.jpg', '').replace('.png', '').replace('.jpeg', '')
            parts = name.split('_')
            
            if len(parts) < 5:
                continue
            
            flags = parts[-5:]
            
            ethnicity = 'unknown'
            gender = 'unknown'
            age = 25
            
            ethnicity_keywords = ['Caucasian', 'Vietnam', 'Indian', 'African', 'Middle', 'East', 'Latino', 'Asian', 'Black']
            
            for part in parts[:-5]:
                part_lower = part.lower()
                if part in ethnicity_keywords:
                    ethnicity = part
                elif part_lower in ['male', 'female']:
                    gender = part_lower
                elif part.isdigit() and int(part) <= 100:
                    age = int(part)
            
            img_path = os.path.join(defects_path, filename)
            img_filename = f"defect_{idx:06d}.jpg"
            save_path = os.path.join(self.output_path, img_filename)
            
            try:
                img = Image.open(img_path).convert('RGB').resize((224, 224))
                img.save(save_path, 'JPEG', quality=85)
                
                save_data.append({
                    'image_path': img_filename,
                    'ethnicity': ethnicity,
                    'gender': gender,
                    'age': age,
                    'acne': int(flags[0]),
                    'acne_marks': int(flags[1]),
                    'stains': int(flags[2]),
                    'wrinkles': int(flags[3]),
                    'dark_circles': int(flags[4]),
                    'source': '4788_defects'
                })
            except:
                continue
        
        print(f"4788 defects processed: {len(save_data)} images")
        return save_data
    
    def process_skin_issues(self):
        """Process Skin Issues dataset (folder-based labels)"""
        print("Processing Skin Issues Dataset...")
        
        issues_path = os.path.join(
            self.base_path,
            'GlowMix',
            'Skin Issues Dataset',
            'Skin v2'
        )
        
        folder_labels = {
            'blackheades': 'acne',
            'dark spots': 'dark_circles',
            'pores': 'texture',
            'wrinkles': 'wrinkles'
        }
        
        save_data = []
        img_counter = 0
        
        for folder in os.listdir(issues_path):
            if folder.startswith('.') or folder not in folder_labels:
                continue
            
            folder_path = os.path.join(issues_path, folder)
            label = folder_labels[folder]
            
            files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
            
            for filename in files:
                img_path = os.path.join(folder_path, filename)
                img_filename = f"issue_{img_counter:06d}.jpg"
                save_path = os.path.join(self.output_path, img_filename)
                
                try:
                    img = Image.open(img_path).convert('RGB').resize((224, 224))
                    img.save(save_path, 'JPEG', quality=85)
                    
                    save_data.append({
                        'image_path': img_filename,
                        'ethnicity': 'unknown',
                        'gender': 'unknown',
                        'age': 30,
                        'acne': 1 if label == 'acne' else 0,
                        'acne_marks': 0,
                        'stains': 1 if label == 'dark_circles' else 0,
                        'wrinkles': 1 if label == 'wrinkles' else 0,
                        'dark_circles': 1 if label == 'dark_circles' else 0,
                        'source': 'skin_issues'
                    })
                    img_counter += 1
                except:
                    continue
        
        print(f"Skin Issues processed: {len(save_data)} images")
        return save_data
    
    def process_all(self):
        """Process all datasets and save unified training data"""
        print("=" * 50)
        print("NAQAL DATA PROCESSING PIPELINE")
        print("=" * 50)
        
        all_data = []
        
        # Process FairFace
        print("\n[1/3]")
        fairface_data = self.process_fairface()
        all_data.extend(fairface_data)
        
        # Process 4788 defects
        print("\n[2/3]")
        defects_data = self.process_4788_defects()
        all_data.extend(defects_data)
        
        # Process Skin Issues
        print("\n[3/3]")
        issues_data = self.process_skin_issues()
        all_data.extend(issues_data)
        
        print(f"\n{'='*50}")
        print(f"Total training samples: {len(all_data)}")
        
        # Save metadata
        output_file = os.path.join(self.output_path, 'naqal_training_data.json')
        with open(output_file, 'w') as f:
            json.dump(all_data, f)
        
        print(f"Metadata saved to: {output_file}")
        print(f"Images saved to: {self.output_path}")
        print(f"{'='*50}")
        
        return len(all_data)