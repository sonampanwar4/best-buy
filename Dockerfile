# Use an official Python runtime
FROM python:3.12-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Display Python output immediately
ENV PYTHONUNBUFFERED=1

# Copy dependency file first (if it exists)
COPY . /app

# Set working directory
WORKDIR /app

# Install dependencies (if requirements.txt exists)
RUN if [ -f requirements.txt ]; then \
        pip install --no-cache-dir -r requirements.txt; \
    fi

# Copy application source
COPY . .

# Run the application
CMD ["python", "main.py"]