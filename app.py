from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from io import BytesIO
from img_generation import generate_image, generate_image_twitter
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

@app.get("/generate_image/")
async def generate_image_endpoint(name: str, num: str):
    # 이미지 생성
    num = int(num)
    img = generate_image(name, num)

    # 이미지를 메모리에서 바로 반환할 수 있도록 BytesIO로 변환
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    # 이미지 반환
    return StreamingResponse(img_io, media_type="image/png")

@app.get("/generate_image/twitter/")
async def generate_image_endpoint_twitter(name: str, num: str):
    # 이미지 생성
    num = int(num)
    img = generate_image_twitter(name, num)

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

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)