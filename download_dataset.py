import os
from roboflow import Roboflow

def automated_dataset_download():
    print("Downloading Skin Problem Detection dataset...")
    
    rf = Roboflow(api_key="NGiVYSKFQ9ZR7L8IRX8y")
    
    project = rf.workspace("parin-kittipongdaja-vwmn3").project("skin-problem-detection-relabel-clean3")
    
    print("Downloading images and labels...")
    dataset = project.version(2).download("yolov8")
    
    print(f"Done! Location: {dataset.location}")

if __name__ == "__main__":
    automated_dataset_download()