# tests/test_app.py
import pytest
import sys
import os

# app.py를 import할 수 있도록 경로 추가
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app import app

@pytest.fixture
def client():
    """Flask 테스트 클라이언트 생성"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """메인 페이지 테스트"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data
    assert 'status' in data
    assert data['status'] == 'running'

def test_home_message_content(client):
    """메시지 내용 확인"""
    response = client.get('/')
    data = response.get_json()
    assert 'Hello' in data['message'] or 'CI/CD' in data['message']

def test_response_format(client):
    """응답 형식 검증"""
    response = client.get('/')
    assert response.content_type == 'application/json'
