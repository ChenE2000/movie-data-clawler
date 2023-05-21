import base64
from io import BytesIO
from PIL import Image, ImageOps

def add_margin(base64_image: str):
    # 解码base64图片字符串为字节数据
    image_data = base64.b64decode(base64_image)

    # 将字节数据加载为图像对象
    image = Image.open(BytesIO(image_data))

    # 计算添加边框后的图像尺寸
    new_width = image.width + 40  # 每个边增加20px
    new_height = image.height + 40

    # 将填充颜色转换为RGB格式
    fill_color = (70, 57, 103)  # RGB颜色值为(70, 57, 103)

    # 创建新的带有边框颜色的图像
    bordered_image = ImageOps.expand(image, border=(20, 20, 20, 20), fill=fill_color)

    # 将边框图像转换为Base64编码的字符串
    buffered = BytesIO()
    bordered_image.save(buffered, format="PNG")
    base64_bordered_image = base64.b64encode(buffered.getvalue()).decode("utf-8")
    # save to file
    # with open("figure_margin.png", "wb") as f:
    #     f.write(buffered.getvalue())
    return base64_bordered_image