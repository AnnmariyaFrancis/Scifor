import streamlit as st
import cv2
import numpy as np
import imutils
import easyocr
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow import keras

# Define the input image size for both apps
image_size = (224, 224)

# Load the signal violation detection model
signal_model = keras.applications.MobileNetV2(input_shape=image_size + (3,), include_top=False, weights='imagenet')
signal_model.trainable = False

x = GlobalAveragePooling2D()(signal_model.output)
x = Dense(1024, activation='relu')(x)
predictions = Dense(1, activation='sigmoid')(x)

signal_detection_model = Model(inputs=signal_model.input, outputs=predictions)
signal_detection_model.load_weights('signal.h5')

# Load the helmet detection model
helmet_cascade = cv2.CascadeClassifier(r'haarcascade_helmet.xml')

font = cv2.FONT_HERSHEY_SIMPLEX

st.title("Combined Detection App")

# Choose the section based on user input
app_option = st.radio("Select an option:", ("Red Light Signal Violation Detection", "Helmet Detection and License Plate Extraction"))

if app_option == "Red Light Signal Violation Detection":
    st.title("Red Light Signal Violation Detection")

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        new_image = image.load_img(uploaded_image, target_size=image_size)
        new_image = image.img_to_array(new_image)
        new_image = np.expand_dims(new_image, axis=0)
        new_image = new_image / 255.0

        predictions = signal_detection_model.predict(new_image)
        binary_prediction = (predictions > 0.5).astype(int)

        if binary_prediction[0] == 1:
            st.image(uploaded_image, caption="Signal Violation Detected", use_column_width=True)
            st.write("The model predicted a signal violation for the image.")
        else:
            st.image(uploaded_image, caption="No Signal Violation Detected", use_column_width=True)
            st.write("The model predicted no signal violation for the image")

elif app_option == "Helmet Detection and License Plate Extraction":
    st.title("Helmet Detection and License Plate Extraction")

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_image is not None:
        img = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)
        conv_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        st.image(conv_img, use_column_width=True, caption="Original Image")

        img_gray = cv2.cvtColor(conv_img, cv2.COLOR_BGR2GRAY)

        for i in range(1, 100):
            plates = helmet_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=i, minSize=(60, 60))
            if len(plates) == 1:
                (x, y, w, h) = plates[0]
                cv2.rectangle(img, (x, y), (x + 2 * w, y + 2 * h), color=(0, 255, 0), thickness=2)
                st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), use_column_width=True, caption="Image with Detected Helmet")
                break

        if len(plates) == 0:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
            edged = cv2.Canny(bfilter, 30, 200)
            keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(keypoints)
            contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
            location = None
            for contour in contours:
                approx = cv2.approxPolyDP(contour, 10, True)
                if len(approx) == 4:
                    location = approx
                    break
            if location is not None:
                mask = np.zeros(gray.shape, np.uint8)
                new_image = cv2.drawContours(mask, [location], 0, 255, -1)
                new_image = cv2.bitwise_and(img, img, mask=mask)
                (x, y) = np.where(mask == 255)
                (x1, y1) = (np.min(x), np.min(y))
                (x2, y2) = (np.max(x), np.max(y))
                cropped_image = gray[x1:x2 + 1, y1:y2 + 1]
                reader = easyocr.Reader(['en'])
                result = reader.readtext(cropped_image)

                text = ''
                for i in range(0, len(result)):
                    new_text = result[i][-2]
                    text += new_text

                text_position = (location[0][0][0], location[1][0][1] - 20)
                res = cv2.putText(img, text=text, org=text_position, fontFace=font, fontScale=1, color=(255, 255, 255), thickness=4, lineType=cv2.LINE_AA)
                res = cv2.rectangle(img, tuple(location[0][0]), tuple(location[2][0]), (0, 255, 0), 2)
                plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
                st.image(cv2.cvtColor(res, cv2.COLOR_BGR2RGB), use_column_width=True, caption="Image with Extracted License Plate and Text")
            else:
                st.image(img, use_column_width=True, caption="No helmet and license plate is detected")
                plt.imshow(img)
