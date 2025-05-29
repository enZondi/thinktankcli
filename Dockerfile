# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app/ app/

# Expose the port the app runs on
EXPOSE 8080

# Run the app with Gunicorn
CMD ["gunicorn", "--chdir", "app", "main:app", "--bind", "0.0.0.0:8080"]
