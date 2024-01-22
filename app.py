import cv2
import streamlit as st
from yolo_com_od import detect_objects

st.title("Webcam Live Feed")
run = st.checkbox('Run')
frame_list = []
FRAME_WINDOW = st.image(frame_list)
camera = cv2.VideoCapture(0)

while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    frame = detect_objects(frame)

    FRAME_WINDOW.image(frame)
    frame_list.clear()  # Clear the frame list after displaying each frame
    print(len(frame_list))  
else:
    st.write('Stopped')
    
