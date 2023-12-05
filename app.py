from flask import Flask, request, jsonify, render_template, send_from_directory
from Main import NewImg

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

    # Return a response as JSON
    NewImg(xt, yt, zt, punten, slider1Value, slider2Value, slider3Value)

    response_data = {
        'message': 'Data received and processed successfully.'
    }
    return jsonify(response_data)

@app.route('/')
def index():
    return render_template('website.html')  # Replace with your actual HTML file


@app.route('/images/<filename>')
def image(filename):
    return send_from_directory('static', filename)


if __name__ == '__main__':
    app.run(debug=True)
