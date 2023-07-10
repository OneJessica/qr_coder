from utils.qr_code import get_qr
import streamlit as st
st.title('二维码生成器')

with st.form('qr_coder'):
    text = st.text_input('二维码内容')
    color = st.color_picker(label='背景颜色',value = '#f5f7f5')
    fill = st.color_picker(label='填充颜色',)
    filename = 'text.png'

    if st.form_submit_button('生成'):
        if not text:
            st.error('请输入二维码内容')
            st.stop()
        get_qr(text,filename,fill=fill,color=color)
        st.image(filename)