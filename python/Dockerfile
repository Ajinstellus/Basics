###############
# Stage 1: Build
###############
FROM python:3.10-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy requirement file
COPY requirements.txt .

# Install Python packages to a temp directory
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --prefix=/install -r requirements.txt


#######################
# Stage 2: Production
#######################
FROM python:3.10-slim

WORKDIR /app

# Copy installed packages from builder image
COPY --from=builder /install /usr/local

# Copy application code
COPY . .

# Expose port
EXPOSE 5000

# Start the app using Gunicorn (production WSGI server)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

