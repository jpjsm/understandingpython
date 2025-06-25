from PIL import Image
from pathlib import Path

me_path = Path(__file__).parent.resolve().joinpath("me.jpg")


def ShowMe():
    # Open the image
    image = Image.open(me_path)
    img_width, img_height = image.size
    if img_width > 640:
        ratio = 640 / img_width
        new_width = int(img_width * ratio)
        new_height = int(img_height * ratio)
        new_img = image.resize((new_width, new_height))
    elif img_height > 640:
        ratio = 640 / img_height
        new_width = int(img_width * ratio)
        new_height = int(img_height * ratio)
        new_img = image.resize((new_width, new_height))
    else:
        new_img = image.copy()

    # demo img need to be rotated
    new_img = new_img.rotate(90)
    # Display the image
    new_img.show()


if __name__ == "__main__":
    ShowMe()
    print(f"{'*'*40}  DONE !!  {'*'*40}")
