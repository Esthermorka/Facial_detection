# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:25:54 2023

@author: Admin
"""

import streamlit as st
from face_app import detect_faces,face_cascade,cap
import cv2

def main():
    
    st.title('Face Dectection app')
    
    detect_faces()
    
if __name__ == '__main__':
        main()