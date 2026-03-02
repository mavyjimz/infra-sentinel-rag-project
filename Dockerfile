# Use a lightweight Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies for ChromaDB and Python
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Environment variables will be handled via docker-compose or .env
ENV PYTHONUNBUFFERED=1

# Default command to run the security check
CMD ["python3", "scripts/p11-security.py"]
