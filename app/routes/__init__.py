from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.auth import router as auth_router
from app.routes.face_analysis import router as face_router
from app.routes.product_scan import router as product_router
from app.routes.unified_scan import router as unified_router
from app.routes.ocr_scan import router as ocr_router

app = FastAPI(title="Naqal API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
app.include_router(face_router, prefix="/api/face", tags=["face"])
app.include_router(product_router, prefix="/api/product", tags=["product"])
app.include_router(unified_router, prefix="/api/scan", tags=["unified"])
app.include_router(ocr_router, prefix="/api/ocr", tags=["ocr"])

@app.get("/")
async def root():
    return {"message": "Naqal API is running", "status": "ok"}