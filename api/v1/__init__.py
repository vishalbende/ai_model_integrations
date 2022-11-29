from .gptj6b import router as gpt6_router
from .stable_defusion2 import router as stable_defusion_router
from fastapi import APIRouter
router = APIRouter(prefix="/v1", tags=["ai models"])
router.include_router(gpt6_router)
router.include_router(stable_defusion_router)
