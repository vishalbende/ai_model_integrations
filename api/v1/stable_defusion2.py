

from pydantic import BaseModel
from fastapi import APIRouter
from starlette.responses import JSONResponse
import requests
from settings import HUGGINGFACE_STABLE_DIFFUSION_API_URL, HUGGINGFACE_API_TOKEN


class Item(BaseModel):
    input_string: str


router = APIRouter(prefix="/stable_defusion2")



@router.post('/')
def get_inference(args: Item):
    API_URL = HUGGINGFACE_STABLE_DIFFUSION_API_URL
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

    response = requests.post(API_URL, headers=headers, json={
        "inputs": args.input_string

    })

    return JSONResponse(status_code=200, content=response.json())