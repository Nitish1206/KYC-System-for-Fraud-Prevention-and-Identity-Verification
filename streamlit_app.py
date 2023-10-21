import streamlit as st
import cv2
import numpy as np
from PIL import Image
from face_recognition.face_recognition_helper import *
# from streamlit_webrtc import VideoTransformerBase, webrtc_streamer
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration, VideoTransformerBase,WebRtcMode
import threading
from typing import Union
import av
import os
import aiortc
from sample_utils.turn import get_ice_servers
import queue
import multiprocessing
from multiprocessing import Process,Manager
import tensorflow as tf


# class StreamlitUI:
#     def __init__(self):
def streamlitui():
    model=LoadModel()
    # model=d["model"]


    # if "reco_obj" not in st.session_state:
    #     print("setting model object....")
    #     st.session_state.reco_obj = Face_recogntion()

        
    st.title("Document Upload Form")

    # Radio button to select PAN card or Aadhar Card
    card_choice = st.radio("Select Card Type", ("PAN Card", "Aadhar Card"))

    # Common fields for both card types
    name = st.text_input("Name")
    address = st.text_input("Address")
    phone_number = st.text_input("Phone Number")
    dob = st.date_input("Date of Birth")
    gender = st.selectbox("Gender", ("Male", "Female", "Other"))
    father_name = st.text_input("Father's Name")
    mother_name = st.text_input("Mother's Name")
    image_upload = st.file_uploader("Upload an Image")

    # Fields specific to PAN card
    if card_choice == "PAN Card":
        pan_number = st.text_input("PAN Card Number")

    # Fields specific to Aadhar card
    if card_choice == "Aadhar Card":
        aadhar_number = st.text_input("Aadhar Card Number")

    # Submit button
    if st.button("Submit"):
        status="Failed"
        if image_upload is not None:
        # Read the image using OpenCV
            image = Image.open(image_upload)
            # print(type(image))
            img_array = np.array(image)
            cv2.imwrite('out.jpg', cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR))
            img_array=cv2.imread("out.jpg")
            status,image=model.detect_and_store_embedding(img_array,"aadhar")

        st.success("Form Submitted Successfully!"+ str(status))
        

    if "last_captured_frame" not in st.session_state:
        st.session_state.last_captured_frame = None

    st.title("Webcam Display Steamlit App")
    st.caption("Powered by OpenCV, Streamlit")


    # st.title("Video Stream")
    # result_queue: "queue.Queue[List[Detection]]" = queue.Queue(max=1)
    frame_queue = Queue(maxsize=1)

    class VideoTransformer(VideoTransformerBase):
            frame_lock: threading.Lock  # `recv()` is running in another thread, then a lock object is used here for thread-safety.
            
            out_image: Union[np.ndarray, None]

            def __init__(self) -> None:
                self.frame_lock = threading.Lock()
                
                self.out_image = None

            def transform(self, frame: av.VideoFrame) -> np.ndarray:
                out_image = frame.to_ndarray(format="bgr24")

                with self.frame_lock:
                    
                    self.out_image = out_image
                return out_image

    webrtc_ctx = webrtc_streamer(
                                    key="object-detection",
                                    mode=WebRtcMode.SENDRECV,
                                    rtc_configuration={
                                                        "iceServers": get_ice_servers(),
                                                        "iceTransportPolicy": "relay",
                                                    },
                                    video_processor_factory=VideoTransformer,
                                    media_stream_constraints={"video": True, "audio": False},
                                    async_processing=True,
                                )
    # while True:
                # if webrtc_ctx.video_transformer:    
                #     result = webrtc_ctx.video_transformer.result_queue.get()
                #     labels_placeholder.table(result)
                # else:
                #     break

    if webrtc_ctx.video_transformer:

            snap = st.button("Snapshot")
            if snap:
                with webrtc_ctx.video_transformer.frame_lock:
                    out_image = webrtc_ctx.video_transformer.out_image

                if out_image is not None:
                    
                    st.write("Output image:")
                    st.image(out_image, channels="BGR")
                    my_path = os.path.abspath(os.path.dirname(__file__))
                    print("my path,")  
                    image_path= my_path+os.sep+"verification"+os.sep+"filename.jpg"
                    
                    cv2.imwrite(image_path, out_image)
                    image=cv2.imread(image_path)
                    st.session_state.last_captured_frame=image.copy()

                else:
                    st.warning("No frames available yet.")


    verify = st.button("Verify")

    if verify:
        last_captured_frame = st.session_state.last_captured_frame

        # print("last cap ===>>>",last_captured_frame)

        if last_captured_frame is not None:
            st.subheader("Last Captured Image")
            st.image(last_captured_frame, channels="BGR", use_column_width=True)

            status,image=model.detect_and_store_embedding(last_captured_frame,"live")

            status,acc=model.find_similarity()
            if acc > 0.5:
                st.success("auth  Successfully!"+ str(status) + "  "+  str(acc))
            else:
                st.error("auth failed!"+ str(status) + "  "+  str(acc))

@st.cache_resource 
def LoadModel():
    model=Face_recogntion()
    return model




# def LoadModel(d):
#     print("loading model")
#     model=Face_recogntion()
#     time.sleep(5)
#     print("model loading done...")
#     d["model"]=model
    

if __name__ == '__main__':
    # StreamlitUI()
    # model=Face_recogntion()
    streamlitui()
    # multiprocessing.set_start_method('spawn')
    # with Manager() as manager:
    #     d = manager.dict()
    #     p = Process(target=LoadModel, args=(d,))
    #     p.start()
    #     p.join()
    #     p2=Process(target=StreamlitUI,args=(d,))
    #     p.start()
    #     p.join()