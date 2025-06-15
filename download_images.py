import os
import requests
from PIL import Image
from io import BytesIO

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img = img.resize((240, 240))  # Resize to match our template
        img.save(filename)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {filename}")

# Create media directory if it doesn't exist
os.makedirs('media/course_images', exist_ok=True)

# Download images for each course
images = {
    'python.jpg': 'https://raw.githubusercontent.com/python/peps/main/pep-0008/pep-0008.jpg',
    'web.jpg': 'https://raw.githubusercontent.com/mdn/beginner-html-site/gh-pages/images/firefox-icon.png',
    'data.jpg': 'https://raw.githubusercontent.com/scikit-learn/scikit-learn/main/doc/sklearn-logo.png'
}

for filename, url in images.items():
    download_image(url, f'media/course_images/{filename}') 