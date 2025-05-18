# Number Plate Detection of Vehicles

This project demonstrates an end-to-end Python application for **Number Plate Detection of Vehicles** using OpenCV and Tesseract OCR. The script processes a car image, detects the license plate using contour detection, and extracts the text using OCR. The result is saved to a CSV file with a timestamp.

## 📸 How it Works

 1. Loads a video (`input.mp4`) instead of webcam.
 2. Detects hand regions using HSV color space.
 3. Finds contours and convexity defects.
 4. Counts fingers based on angles between defects.
 5. Displays the detected gesture on each frame.


## 🔧 Requirements

- Python 3.8 or later  
- OpenCV  
- NumPy

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip
- Tesseract OCR (download and install from [here](https://github.com/tesseract-ocr/tesseract))

### Python Packages

Install required libraries using pip:

pip install opencv-python imutils pytesseract pandas
## Features

- Reads and resizes vehicle images.
- Converts image to grayscale and applies filters for noise reduction.
- Detects edges and identifies the license plate via contour detection.
- Extracts license plate region using masking.
- Uses Tesseract OCR to recognize text from the license plate.
- Saves results with a timestamp into a CSV file.

## Usage

- Replace the image path in the script with your own image:

    image = cv2.imread(r'path_to_your_image.jpg')
- Run the Python script:

    python license_plate_recognition.py
- The script will:

   1. Display intermediate image processing results.

   2. Print the detected text from the license plate.

   3. Append the text and timestamp to a data.csv file.





## License

[MIT](https://choosealicense.com/licenses/mit/)


## Acknowledgements

- Tesseract OCR: Open-source OCR engine developed by Google.

- OpenCV: Powerful library for computer vision tasks.

- imutils: Useful utilities for image processing.

- Inspired by various open-source ALPR implementations available on GitHub.



## Feedback

If you have any feedback, please reach out to us at For questions or improvements, feel free to reach out:

📩 Email: harishlm2005@gmail.com

🌐 GitHub: https://github.com/harishlm05


