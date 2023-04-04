import requests
import io
import ascii_magic
from PIL import Image
from ascii_magic import AsciiArt, from_image

# Download the image from the URL
url = "https://i.pinimg.com/originals/59/71/45/5971451d29591be5030a4125d1adc9dc.jpg"
response = requests.get(url)

# Save the image in the same directory as the script
with open('putin.jpg', 'wb') as f:
    f.write(response.content)

# Load the image
with Image.open('putin.jpg') as image:
    # Calculate the new dimensions based on the desired width while maintaining aspect ratio
    width = 200
    aspect_ratio = float(image.width) / float(image.height)
    height = int(width / aspect_ratio)

    # Resize the image while keeping the aspect ratio
    image = image.resize((width, height))

    # Save the resized image to a temporary file
    temp_file_path = 'temp_resized_putin.jpg'
    image.save(temp_file_path)

# Create an AsciiArt object using the from_image() function
my_art = from_image(temp_file_path)

# Save the ASCII art to an HTML file
my_art.to_html_file('ascii_art.html', columns=200, width_ratio=2)

# Remove the temporary file
import os
os.remove(temp_file_path)
