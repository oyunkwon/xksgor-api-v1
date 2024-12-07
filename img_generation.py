from PIL import Image, ImageFont, ImageDraw

# 이미지 로드
def generate_image(name, num):
    target_img = Image.open("static/template.png")

    def loadfont(fontsize=50):
    # ttf 파일의 경로를 지정
        ttf = 'static/Pretendard-Bold.ttf'
        return ImageFont.truetype(font=ttf, size=fontsize)


    namefontObj = loadfont(fontsize=120)
    numfontObj = loadfont(fontsize=83)
    out_img = ImageDraw.Draw(target_img)
    numStr = f"#{num:,}"
    num_bbox = out_img.textbbox((0, 0), numStr, font=numfontObj)
    text_width, text_height = num_bbox[2] - num_bbox[0], num_bbox[3] - num_bbox[1]
    out_img.text(xy=(214, 220), text=name, fill=(255, 255, 255), font=namefontObj)
    out_img.text(xy=(858 - text_width, 1562), text=numStr, fill=(255, 81, 0), font=numfontObj)
    return target_img


def generate_image_twitter(name, num):
    target_img = Image.open("static/template-twitter.png")

    def loadfont(fontsize=50):
        # ttf 파일의 경로를 지정
        ttf = 'static/Pretendard-Bold.ttf'
        return ImageFont.truetype(font=ttf, size=fontsize)


    namefontObj = loadfont(fontsize=120)
    numfontObj = loadfont(fontsize=83)
    out_img = ImageDraw.Draw(target_img)
    numStr = f"#{num:,}"
    num_bbox = out_img.textbbox((0, 0), numStr, font=numfontObj)
    text_width, text_height = num_bbox[2] - num_bbox[0], num_bbox[3] - num_bbox[1]
    out_img.text(xy=(160, 60), text=name, fill=(255, 255, 255), font=namefontObj)
    out_img.text(xy=(1020 - text_width, 400), text=numStr, fill=(255, 81, 0), font=numfontObj)
    return target_img
