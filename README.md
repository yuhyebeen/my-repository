# AWS EC2 Streamlit Deployment Assignment

## 과제 개요
AWS Academy Learner Lab의 EC2 환경에서 Streamlit 앱을 실행하고, EC2 Public IPv4 주소를 통해 외부 브라우저에서 접속 가능한지 확인하는 실습입니다.

## 실행 환경
- AWS Academy Learner Lab
- EC2 Ubuntu
- Python
- Streamlit

## 실행 방법

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m streamlit run app.py --server.port 8501 --server.address 0.0.0.0
