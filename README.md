Steps to run:

1. Git Clone this repo
2. pip install -r requirements.txt
3. python app.py
4. Now Backend API is running

API DOCS:
2 endpoints

# API Documentation

## 1. Picture Inference API

**Endpoint:** `/api/inferpic`

**Method:** `POST`

**Description:** This API endpoint accepts an image file, processes it, and returns the processed image.

**Request:**

The request should contain a file data with the key 'file'. The file should be an image with one of the following extensions: 'png', 'jpg', 'jpeg', 'gif'.

**Response:**

If successful, the API will return the processed image file. If the request does not contain a file, or the file is empty, or the file is not an image, the API will return an error message with a 400 status code.

---

## 2. Inference API

**Endpoint:** `/api/infer`

**Method:** `POST`

**Description:** This API endpoint accepts an image file, processes it, and returns the keypoint coordinates.

**Request:**

The request should contain a file data with the key 'file'. The file should be an image with one of the following extensions: 'png', 'jpg', 'jpeg', 'gif'.

**Response:**

If successful, the API will return a JSON object containing the keypoint coordinates. If the request does not contain a file, or the file is empty, or the file is not an image, the API will return an error message with a 400 status code.