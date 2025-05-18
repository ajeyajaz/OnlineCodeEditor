# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Navigate to the directory containing manage.py
WORKDIR /app/codebackend

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Django port
EXPOSE 8000

# Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
