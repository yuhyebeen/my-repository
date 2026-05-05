import streamlit as st

st.title("AWS EC2 Streamlit 배포 실습")
st.write("이 앱은 AWS Learner Lab EC2 환경에서 실행 중입니다.")

name = st.text_input("이름을 입력하세요")

if st.button("결과 확인"):
    st.success(f"{name}님, 앱이 정상적으로 실행되었습니다!")
