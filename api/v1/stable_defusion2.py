

from pydantic import BaseModel
from fastapi import APIRouter
from starlette.responses import JSONResponse
import requests
from settings import HUGGINGFACE_STABLE_DIFFUSION_API_URL, HUGGINGFACE_API_TOKEN
from fastapi.responses import FileResponse


from diffusers import DiffusionPipeline
import torch
#pipeline = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2")

from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler

model_id = "stabilityai/stable-diffusion-2"

# Use the Euler scheduler here instead
scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, revision="fp16", torch_dtype=torch.float16)
pipe = pipe.to("cuda")


class Item(BaseModel):
    input_string: str


router = APIRouter(prefix="/stable_defusion2")



@router.post('/')
def get_inference(args: Item):
    # API_URL = HUGGINGFACE_STABLE_DIFFUSION_API_URL
    # headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

    # response = requests.post(API_URL, headers=headers, json={
    #     "inputs": args.input_string

    # })
    prompt = args.input_string
    image = pipe(prompt, height=768, width=768).images[0]
    image.save('static/main_image.png')

    return FileResponse('static/main_image.png')