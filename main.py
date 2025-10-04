import qrcode
import streamlit as st
import io
# import lib

st.markdown("""
    <style>
    .stButton > button {
        background-color: #4CAF50; /* Green */
        width: 100%;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        font-size: 16px;
        font-weight: bold;
        border: none;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# ===================== USER INPUT ==================== #

# กำหนดชื่อไฟล์และข้อมูลที่ต้องการสร้าง QR Code
# filename = "example"  # ชื่อไฟล์ QR Code
# data = "Description: example"  # URL or Text

# Input for streamlit
filename = st.text_input('Filename (without extension)', 'example')

mode = st.radio("เลือกวิธีใส่ข้อมูล", ["Input text", "Upload file"])

data = None
if mode == "Input text":
    data = st.text_input('Input text or URL')
elif mode == "Upload file":
    uploaded_file = st.file_uploader("Upload File")
    if uploaded_file:
        data = uploaded_file.read().decode("utf-8")

if st.button('Create QR Code') and data:
    # สร้าง QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")


    # แปลงเป็น BytesIO เพื่อดาวน์โหลด
     # แปลงเป็น BytesIO เพื่อใช้กับ st.image
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    # แสดงผลใน streamlit
    st.image(buf.getvalue())
    buf.seek(0)

    st.download_button(
        label="Download QR Code",
        data=buf,
        file_name=f"{filename}.png",
        mime="image/png"
    )
