from PIL import Image
import pyocr
from pyocr import tesseract

tool = tesseract

def image_to_string( input_image: Image ):
    image_text = tool.image_to_string(
        input_image,
        lang='jpn+eng',
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )
    return image_text
