-- 사용자 테이블 생성
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

-- 샘플 데이터 추가
INSERT INTO users (name, email) VALUES
    ('nayatrei', 'nayatrei3@naver.com'),
    ('kaero313', 'kaero313@naver.com'),
    ('yj', 'https://kaero313.github.io/posts/docker_2/');
