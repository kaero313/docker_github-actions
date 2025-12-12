# ============================================
# 빌드 스테이지: gcc로 패키지 컴파일
# ============================================
FROM python:3.11-slim AS builder

WORKDIR /app

# 빌드 도구만 설치
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Python 패키지 설치
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt


# ============================================
# 실행 스테이지: 런타임만 포함
# ============================================
FROM python:3.11-slim

WORKDIR /app

# 런타임 라이브러리만 설치 (gcc 제외!)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# 빌드된 패키지만 복사
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# 소스 코드 복사
COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
