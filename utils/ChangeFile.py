import os

from PIL import Image


class ImageEditor:

    @staticmethod
    def reduce_image(file_path, width, height):
        allowed_file_formats = (".jpg", ".jpeg", ".gif", ".png")
        file_ext = os.path.splitext(file_path)[-1].lower()
        if file_ext not in allowed_file_formats:
            return
        with Image.open(file_path) as img:
            if img.height > height or img.width > width:
                image_size = (width, height)
                img.thumbnail(image_size)
                img.save(file_path)