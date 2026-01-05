# 간단한 Flask 웹 애플리케이션
from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# 데이터베이스 연결 정보
DB_HOST = os.getenv('DB_HOST', 'postgres')
DB_NAME = os.getenv('DB_NAME', 'myapp')
DB_USER = os.getenv('DB_USER', 'user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')

def get_db_connection():
    """PostgreSQL 연결"""
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

@app.route('/')
def home():
    """메인 페이지"""
    return jsonify({
        'message': 'Hello Docker Compose! I am nayatrei.',
        'status': 'running',
        'user': 'nayatrei'
    })

@app.route('/users')
def get_users():
    """데이터베이스에서 사용자 목록 조회"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, email FROM users;')
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        
        # 결과를 JSON으로 변환
        users_list = []
        for user in users:
            users_list.append({
                'id': user[0],
                'name': user[1],
                'email': user[2]
            })
        
        return jsonify({'users': users_list})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # 모든 인터페이스에서 접근 가능하도록 설정
    app.run(host='0.0.0.0', port=5000)

def test_should_fail():
    """일부러 실패하는 테스트"""
    assert 1 == 2  # 무조건 실패!
