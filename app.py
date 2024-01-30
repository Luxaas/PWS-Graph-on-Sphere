from flask import Flask, request, jsonify, render_template, send_from_directory
from Main import NewImg
import numpy as np
from io import BytesIO
from PIL import Image

def image_to_bytes(image):
    # Convert PIL Image to bytes
    image_io = BytesIO()
    image.save(image_io, format='PNG')
    image_bytes = image_io.getvalue()
    return image_bytes

app = Flask(__name__)

@app.route('/process-data', methods=['POST'])
def process_data():
    # Get the data sent by the website as JSON
    data = request.json

    # Access individual data fields
    xt = data.get('xt')
    yt = data.get('yt')
    zt = data.get('zt')
    punten = data.get('punten')
    slider1Value = data.get('slider1Value')
    slider2Value = data.get('slider2Value')
    slider3Value = data.get('slider3Value')



    # Process the data as needed
    # You can perform calculations or any other operations here
    
    # Return the image as bytes
    image = generate_image(xt, yt, zt, punten, slider1Value, slider2Value, slider3Value)
    image_bytes = image_to_bytes(image)
    return image_bytes

@app.route('/')
def index():
    return render_template('website.html')  # Replace with your actual HTML file

@app.route('/images/<filename>')
def image(filename):
    return send_from_directory('static', filename)

def generate_image(xt, yt, zt, punten, slider1Value, slider2Value, slider3Value):
    Pixels = NewImg(xt, yt, zt, punten, slider1Value, slider2Value, slider3Value)
    array = np.array(Pixels, dtype=np.uint8)
    new_image = Image.fromarray(array)
    return new_image

if __name__ == '__main__':
    app.run(debug=True)
