from PIL import Image


class ImageEditor:

    @staticmethod
    def reduce_image(file_path, width, height):
        with Image.open(file_path) as img:
            if img.height > height or img.width > width:
                image_size = (width, height)
                img.thumbnail(image_size)
                img.save(file_path)