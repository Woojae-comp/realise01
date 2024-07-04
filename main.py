import streamlit as st
from PIL import Image
from exchange_module import ex_rate
from melon_lyrics import scrape_lyrics
import national_pension as np
from font import set_korean_font 


# 사이드바 화면

set_korean_font()

st.sidebar.header("로그인")
user_id = st.sidebar.text_input('아이디(ID) 입력', value="streamlit", max_chars=15)
user_password = st.sidebar.text_input('패스워드(Password) 입력', value="", type="password")

if user_id == 'chawj91' and user_password == '1234':
    st.sidebar.header("Project")
    selectbox_options = ['환율조회', '가사검색', '데이터분석', '탐색적데이터분석', '머신러닝'] # 셀렉트 박스의 선택 항목
    your_option = st.sidebar.selectbox('**Menu**', selectbox_options) # 셀렉트박스의 항목 선택 결과

    if your_option == '환율조회':
        st.subheader("환율조회")
        ex_rate()

    elif your_option == '탐색적데이터분석':
        st.write("탐색적데이터분석")
        np.np_main()
  
    elif your_option == '머신러닝':
        st.write('머신러닝')

    elif your_option == '가사검색':
        st.subheader("가사검색")
        singer = st.text_input("가수 이름을 입력하세요:")
        if st.button("크롤링 시작"):
            if singer:
                with st.spinner("크롤링 중... 잠시만 기다려주세요."):
                    data = scrape_lyrics(singer)
                    st.success("크롤링 완료!")
                    st.dataframe(data)
            else:
                st.error("가수 이름을 입력하세요.")

    elif your_option == '데이터분석':
        pass

    else:
        st.write('환영합니다!')



    