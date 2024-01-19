from PIL import Image
from io import BytesIO

def load_image(image):
    return Image.open(BytesIO(image))
