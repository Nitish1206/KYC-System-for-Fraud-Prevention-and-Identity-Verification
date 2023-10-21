import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration, VideoTransformerBase,WebRtcMode
import av
import numpy as np
import aiortc
import cv2
from sample_utils.turn import get_ice_servers
# from streamlit_webrtc import WebRtcMode, webrtc_streamer
from queue import Queue
import threading
from typing import Union
import av
import os
# Create a Streamlit app
st.title("Video Stream")
# result_queue: "queue.Queue[List[Detection]]" = queue.Queue(max=1)
frame_queue = Queue(maxsize=1)

class VideoTransformer(VideoTransformerBase):
        frame_lock: threading.Lock  # `transform()` is running in another thread, then a lock object is used here for thread-safety.
        
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
if webrtc_ctx.video_transformer:

        snap = st.button("Snapshot")
        if snap:
            with webrtc_ctx.video_transformer.frame_lock:
                out_image = webrtc_ctx.video_transformer.out_image

            if out_image is not None:
                
                st.write("Output image:")
                st.image(out_image, channels="BGR")
                my_path = os.path.abspath(os.path.dirname(__file__))    
                print("my path",my_path)   
                cv2.imwrite(os.path.join(my_path, "../Data/"+"filename.jpg"), out_image)

            else:
                st.warning("No frames available yet.")

# if webrtc_ctx.state.playing:
#     labels_placeholder = st.empty()
    
#     while True:
#         print("playing.....")
#         result = result_queue.get()
        # labels_placeholder.table(result)



# start_button_pressed = st.button("Start")

# cap = cv2.VideoCapture(0)
# frame_placeholder = st.empty()

# stop_button_pressed = st.button("Stop")

# # last_captured_frame = None  # Initialize last_captured_frame to None

# while cap.isOpened() and not stop_button_pressed:
#     if start_button_pressed:
#         ret, frame = cap.read()

#         if not ret:
#             st.write("Video Capture Ended")
#             break
#         # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         # global orgframe
#         # print("frame shape === >>>> ",orgframe.shape)
#         frame_placeholder.image(frame,channels="BGR")

#         st.session_state.last_captured_frame = frame.copy()
        
#     if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
#         break


# cap.release()
# cv2.destroyAllWindows()