FROM python:3.8-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy pipeline scripts
COPY scripts/ /app/scripts/

# Create necessary directories
RUN mkdir -p /app/data /app/model /app/results /app/deployment

# Set entrypoint
ENTRYPOINT ["python"]