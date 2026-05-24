import os
import json
import numpy as np
from datetime import datetime
from app.services.supabase_client import supabase

class ModelTrainer:
    """
    Naqal Continuous Learning Engine
    Stores every scan to improve accuracy for Pakistani/Indian skin types
    """
    
    def __init__(self):
        self.data_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'training_data')
        os.makedirs(self.data_dir, exist_ok=True)
    
    async def save_training_sample(self, image_bytes: bytes, results: dict, metadata: dict = None):
        """Save each scan for future model training"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save image
        image_path = os.path.join(self.data_dir, f"face_{timestamp}.jpg")
        with open(image_path, 'wb') as f:
            f.write(image_bytes)
        
        # Save labels
        label_data = {
            "image": f"face_{timestamp}.jpg",
            "acne_score": results.get("acne_score", 0),
            "redness_score": results.get("redness_score", 0),
            "dark_circles_score": results.get("dark_circles_score", 0),
            "texture_score": results.get("texture_score", 0),
            "hydration_score": results.get("hydration_score", 0),
            "sensitivity_score": results.get("sensitivity_score", 0),
            "estimated_age": results.get("estimated_age", 0),
            "overall_health": results.get("overall_health", 0),
            "metadata": metadata or {},
            "timestamp": timestamp
        }
        
        # Save labels file
        label_path = os.path.join(self.data_dir, f"face_{timestamp}.json")
        with open(label_path, 'w') as f:
            json.dump(label_data, f)
        
        return image_path
    
    def get_training_stats(self) -> dict:
        """Get current training data statistics"""
        files = [f for f in os.listdir(self.data_dir) if f.endswith('.jpg')]
        return {
            "total_samples": len(files),
            "data_directory": self.data_dir,
            "last_updated": datetime.now().isoformat()
        }