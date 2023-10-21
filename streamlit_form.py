import streamlit as st
import cv2
import numpy as np
from PIL import Image
from face_recognition.face_recognition_helper import *

# Initialize Face Recognition Helper
recognition_helper_obj = Face_recogntion()

# Define KYC Validator UI
def kyc_validator():
    st.title("KYC Validator & Fraud Detection")
    st.subheader("Welcome to KYC Validator!")
    # st.image("kyc-logo.png", use_column_width=True)

    st.markdown("**Why Choose KYC Validator?**")
    st.markdown("- Quick & Easy Verification")
    st.markdown("- Enhanced Security")
    st.markdown("- User-Friendly")

    # KYC Form
    st.sidebar.title("KYC Form")
    card_choice = st.sidebar.radio("Select Card Type", ("PAN Card", "Aadhar Card"))

    name = st.sidebar.text_input("Name")
    address = st.sidebar.text_input("Address")
    phone_number = st.sidebar.text_input("Phone Number")
    dob = st.sidebar.date_input("Date of Birth")
    gender = st.sidebar.selectbox("Gender", ("Male", "Female", "Other"))
    father_name = st.sidebar.text_input("Father's Name")
    mother_name = st.sidebar.text_input("Mother's Name")
    image_upload = st.sidebar.file_uploader("Upload an Image")

    if card_choice == "PAN Card":
        pan_number = st.sidebar.text_input("PAN Card Number")
    elif card_choice == "Aadhar Card":
        aadhar_number = st.sidebar.text_input("Aadhar Card Number")

    if st.sidebar.button("Submit"):
        if image_upload is not None:
            image = Image.open(image_upload)
            img_array = np.array(image)
            cv2.imwrite('out.jpg', cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR))
            img_array = cv2.imread("out.jpg")
            status, image = recognition_helper_obj.detect_and_store_embedding(img_array, "aadhar")
        st.success("Form Submitted Successfully!" + str(status))

    # Webcam Capture
    st.sidebar.title("Live Photo Capture")
    start_button_pressed = st.sidebar.button("Start")
    stop_button_pressed = st.sidebar.button("Stop")

    cap = cv2.VideoCapture(0)
    frame_placeholder = st.sidebar.empty()

    while cap.isOpened() and not stop_button_pressed:
        if start_button_pressed:
            ret, frame = cap.read()

            if not ret:
                st.warning("Video Capture Ended")
                break

            frame_placeholder.image(frame, channels="BGR")

            st.session_state.last_captured_frame = frame.copy()

        if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
            break

    cap.release()
    cv2.destroyAllWindows()

    last_captured_frame = st.session_state.last_captured_frame

    if last_captured_frame is not None:
        st.sidebar.subheader("Last Captured Image")
        st.sidebar.image(last_captured_frame, channels="BGR", use_column_width=True)

    if st.sidebar.button("Verify"):
        status, image = recognition_helper_obj.detect_and_store_embedding(last_captured_frame, "live")
        status, acc = recognition_helper_obj.find_similarity()
        if acc > 0.6:
            st.success("Authentication Successful!" + str(status) + "  " + str(acc))
        else:
            st.error("Authentication Failed!" + str(status) + "  " + str(acc))

if __name__ == "__main__":
    kyc_validator()
