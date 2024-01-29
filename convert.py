# Make sure to install Pillow first:
# pip install Pillow

# Replace input.jpg with the name of your JPG file and output.bmp with the desired BMP file name.


from PIL import Image

# Open the JPG file
img = Image.open('input.jpg')

# Save as BMP
img.save('output.bmp')