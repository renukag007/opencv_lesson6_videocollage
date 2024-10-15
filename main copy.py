# Refer - https://www.geeksforgeeks.org/python-create-video-using-multiple-images-using-opencv/

#### Create a Video Collage (Video created out of images)

import os
import cv2
from PIL import Image # Pillow - Image Processing Library Python Imaging Library

# Change the directory as per own folder path where the images are located
os.chdir('/Users/renuka/pics')
path = "/Users/renuka/pics"

mean_height = 0
mean_width = 0

num_of_images = len(os.listdir('.')) # 7

for file in os.listdir('.'):
    img = Image.open(os.path.join(path, file))
    width, height = img.size
    mean_width = mean_width + width
    mean_height = mean_height + height


mean_width = mean_width // num_of_images
mean_height = mean_height // num_of_images

print(mean_width)
print(mean_height)

for file in os.listdir('.'):
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        img = Image.open(os.path.join(path, file))
        width, height = img.size
        print(width, height)

        # imgResized = img.resize((mean_width, mean_height), Image.ANTIALIAS)- Antialias is Deprecated

        imgResized = img.resize((mean_width, mean_height), Image.LANCZOS)
        # Image.LANCZOS is the filter used for high-quality downscaling (previously referred to as ANTIALIAS).
        # The LANCZOS filter is particularly effective when resizing images and provides smooth results, especially when reducing the size.

        imgResized.save(file, 'JPEG', quality = 95)
        print(img.filename.split('\\')[-1], " is resized")

        

def videoGenerator():
    video_name = "RenukaVideo.mp4"  # Ensure this is correct

    os.chdir('/Users/renuka/pics')
    print(f"Current working directory: {os.getcwd()}")


    images = [img for img in os.listdir('.') if img.endswith(('.jpg', '.jpeg', '.png'))]

    if len(images) == 0:
        raise Exception("No image files found to create a video!")

    print("Image files to be used in video:", images)

    # Read the first image to get dimensions
    frame = cv2.imread(os.path.join(".", images[0]))

    # Check if the frame is valid
    if frame is None:
        raise Exception(f"Could not read the image file: {images[0]}")

    height, width, layers = frame.shape

    # Use a valid codec (XVID or MJPG) and ensure proper file extension
    # video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'XVID'), 1, (width, height))
    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), 1, (width, height))


    # Appending the images to the video one by one
    for image in images:
        img_frame = cv2.imread(os.path.join(".", image))
        if img_frame is None:
            print(f"Warning: Could not read {image}, skipping this image.")
            continue
        video.write(img_frame)

    video.release()
    cv2.destroyAllWindows()
    print(f"Video {video_name} created successfully.")


videoGenerator()