"""
Auto-label Cambridge images with acne severity using Roboflow API
Processes ALL 1,522 images with rate limiting
"""

from inference_sdk import InferenceHTTPClient
import os
import json
import time

CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="NGiVYSKFQ9ZR7L8IRX8y"
)

IMAGE_FOLDER = "datasets/skin_type_classification_dataset/train"

# Collect all images
all_images = []
for skin_type in ['oily', 'dry', 'normal', 'combination']:
    folder = os.path.join(IMAGE_FOLDER, skin_type)
    if os.path.exists(folder):
        for f in os.listdir(folder):
            if f.endswith(('.jpg', '.jpeg', '.png')):
                all_images.append(os.path.join(folder, f))

print(f"Total images to label: {len(all_images)}")

# Load existing labels if any
results = {}
label_file = 'datasets/skin_type_classification_dataset/auto_acne_labels.json'
if os.path.exists(label_file):
    with open(label_file) as f:
        results = json.load(f)
    print(f"Existing labels: {len(results)}")

# Auto-label each image
errors = 0
success = 0

for i, img_path in enumerate(all_images):
    # Skip already labeled
    if img_path in results:
        continue
    
    try:
        result = CLIENT.infer(img_path, model_id="acne-gnrti/1")
        
        if 'predictions' in result:
            count = len(result['predictions'])
            severity = min(100, count * 10)
        else:
            count = 0
            severity = 0
        
        results[img_path] = {
            'acne_count': count,
            'acne_severity': severity
        }
        
        success += 1
        print(f"[{success}/{len(all_images)}] {os.path.basename(img_path)[:40]}: {count} spots → severity {severity}")
        
    except Exception as e:
        errors += 1
        err_msg = str(e)[:80]
        print(f"[ERROR {errors}] {os.path.basename(img_path)[:40]}: {err_msg}")
        
        # Save progress on error
        if errors % 10 == 0:
            with open(label_file, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"  💾 Saved {len(results)} labels (backup)")
    
    time.sleep(2)  # Rate limit: 2 seconds between requests
    
    # Save progress every 50 images
    if success % 50 == 0 and success > 0:
        with open(label_file, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"  💾 Saved {len(results)} labels (checkpoint)")

# Final save
with open(label_file, 'w') as f:
    json.dump(results, f, indent=2)

print(f"\n{'='*50}")
print(f"COMPLETE!")
print(f"Total labeled: {len(results)}/{len(all_images)}")
print(f"Success: {success}, Errors: {errors}")
print(f"Saved to: {label_file}")
print(f"{'='*50}")