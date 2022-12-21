import os
from PIL import Image

def read_images(folder):
    return [i for i in os.listdir(folder)]


def image_list(images, folder):
    return [Image.open(f"{folder}/{image}") for image in images]


def animate(frames, filename="video.gif", duration=10, loop=1):
    frames[0].save(filename, save_all=True, append_images=frames[1:], duration=duration, loop=loop)
    

def main():
    screenshot_folder = "screenshots"
    if not os.path.exists(screenshot_folder):
        exit()
    
    images = read_images(screenshot_folder)
    images.sort()    
    print(images)

    im_list = image_list(images, screenshot_folder)
    print(im_list)

    animate(im_list, "video.gif")

    print("\ndone ...")



if __name__ == "__main__":
    main()