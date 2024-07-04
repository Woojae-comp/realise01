import streamlit as st
import matplotlib.pyplot as plt

def set_korean_font():
    """
    Streamlit과 matplotlib에서 한글 폰트를 설정하는 함수.
    """
    # Streamlit 앱에서 폰트 설정
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Nanum Gothic', sans-serif;
        }
        </style>
        """, unsafe_allow_html=True)

    # matplotlib에서 폰트 설정
    plt.rcParams['font.family'] = 'NanumGothic'
    plt.rcParams['axes.unicode_minus'] = False

def main():
    set_korean_font()  # 한글 폰트 설정 함수 호출

    st.title('한글 폰트 테스트')
    st.write('이 앱은 NanumGothic 폰트를 사용합니다.')

    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [4, 5, 6])
    ax.set_title('테스트 플롯')
    st.pyplot(fig)

if __name__ == "__main__":
    main()
