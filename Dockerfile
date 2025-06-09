# Use a Python base image
FROM python:3.12

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    python3-dev \
    curl \
    build-essential \
    postgresql-client \
    netcat-openbsd \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python deps
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /app/

# Make run.sh executable
RUN chmod +x /app/infra/run.sh

# Expose port for Django
EXPOSE 8000

# Run script
CMD ["/bin/bash", "/app/infra/run.sh"]
