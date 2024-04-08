from flask import Flask, request, send_file, jsonify
from PIL import Image
import io
from functions import infer, inferpoints
import cv2

app = Flask(__name__)

# Function to process the image
def process_image(input_image):
    # Example processing: Convert image to grayscale
    processed_image = input_image.convert('L')
    return processed_image

# API endpoint to accept image and return processed image
@app.route('/api/inferpic', methods=['POST'])
def picture_inference_api():    
    # Check if request contains file data

    try:
        if 'file' not in request.files:
            return "No file part in the request", 400
        
        # Get the file from the request
        file = request.files['file']

        # Check if file is empty
        if file.filename == '':
            return "No selected file", 400

        # Check if the file is an image
        if file and allowed_file(file.filename):
            # Open the image file
            input_image = Image.open(io.BytesIO(file.read()))

            # Process the image
            processed_image = infer(input_image)

            # Save the processed image to a temporary file
            temp_file_path = '/tmp/processed_image.jpg'  # Modify this path as needed
            cv2.imwrite(temp_file_path, processed_image)

            # Return the processed image file
            return send_file(temp_file_path, mimetype='image/jpeg')

        else:
            return "Invalid file type. Please upload an image file.", 400
    except Exception as e:
        return e, 500
    

#API endpoint that takes in image and returns keypoint coordinates
@app.route('/api/infer', methods=['POST'])
def inference_api():    
    # Check if request contains file data
    try:
        if 'file' not in request.files:
            return "No file part in the request", 400
        
        # Get the file from the request
        file = request.files['file']

        # Check if file is empty
        if file.filename == '':
            return "No selected file", 400

        # Check if the file is an image
        if file and allowed_file(file.filename):
            # Open the image file
            input_image = Image.open(io.BytesIO(file.read()))

            # Process the image
            keypoints = inferpoints(input_image)
            keypoints = {"keypoints ": keypoints}
            print(type(keypoints))


            return jsonify(keypoints), 200

        else:
            return "Invalid file type. Please upload an image file.", 400
    except Exceptions as e:
        return e, 500

# Helper function to check if the file extension is allowed
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)
