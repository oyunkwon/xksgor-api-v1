from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from io import BytesIO
from img_generation import generate_image
from mangum import Mangum

app = FastAPI()

@app.get("/generate_image/")
async def generate_image_endpoint(name: str, num: int):
    # 이미지 생성
    img = generate_image(name, num)

    # 이미지를 메모리에서 바로 반환할 수 있도록 BytesIO로 변환
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    # 이미지 반환
    return StreamingResponse(img_io, media_type="image/png")

@app.get("/")
async def test():
    # 이미지 생성
    return {"message": "Hello World!"}


handler = Mangum(app)