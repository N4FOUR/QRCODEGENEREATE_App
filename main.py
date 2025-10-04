import qrcode
import streamlit as st
# import lib


# ===================== USER INPUT ==================== #

# กำหนดชื่อไฟล์และข้อมูลที่ต้องการสร้าง QR Code
# filename = "example"  # ชื่อไฟล์ QR Code
# data = "Description: example"  # URL or Text

# Input for streamlit
filename = st.text_input('Filename')
filetype = st.multiselect('FileType', ['File', 'Text'])
if filetype == 'File':
    data = st.file_uploader
else:
    data = st.text_input('Input text or url')


if st.button('Create QR Code'):
    # สร้าง QR Code
    qr = qrcode.QRCode(
        version=1,  # ขนาด QR (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # ความทนทาน
        box_size=10,  # ขนาด box
        border=4,  # ขอบ
    )

    qr.add_data(data)
    qr.make(fit=True)

    # สร้าง image
    img = qr.make_image(fill_color="black", back_color="white")

    st.image(img)
    st.download_button('Download QR Code', img)