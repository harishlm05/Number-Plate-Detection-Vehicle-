import numpy as np
import cv2
import imutils
import pytesseract
import pandas as pd
import time

# Update with correct Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read and resize image
image = cv2.imread(r'C:\Users\user\Downloads\Automatic-License-Plate-Recognition-main\code\image.jpg')
image = imutils.resize(image, width=500)
cv2.imshow("Original Image", image)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Conversion", gray)

# Blur to reduce noise
gray = cv2.bilateralFilter(gray, 11, 17, 17)
cv2.imshow("Bilateral Filter", gray)

# Edge detection
edged = cv2.Canny(gray, 170, 200)
cv2.imshow("Canny Edges", edged)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Find contours
cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]

NumberPlateCnt = None
# Loop over contours to find the license plate
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) == 4:
        NumberPlateCnt = approx
        break

# Create mask and extract plate
mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [NumberPlateCnt], 0, 255, -1)
new_image = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Final Image", new_image)

# Tesseract config
config = ('-l eng --oem 1 --psm 3')

# Run OCR
text = pytesseract.image_to_string(new_image, config=config)

# Save to CSV
raw_data = {'date': [time.asctime(time.localtime(time.time()))], 'text': [text.strip()]}
df = pd.DataFrame(raw_data)
df.to_csv('data.csv', mode='a', index=False)

# Print result
print("Detected Text:", text)

cv2.waitKey(0)
cv2.destroyAllWindows()
