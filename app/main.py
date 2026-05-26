import sys
sys.path.insert(0, '.')

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, face_analysis, product_scan, unified_scan, ocr_scan

app = FastAPI(title="Naqal API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(face_analysis.router, prefix="/api/face", tags=["face"])
app.include_router(product_scan.router, prefix="/api/product", tags=["product"])
app.include_router(unified_scan.router, prefix="/api/scan", tags=["unified"])
app.include_router(ocr_scan.router, prefix="/api/ocr", tags=["ocr"])

@app.get("/")
async def root():
    return {"message": "Naqal API is running", "status": "ok"}