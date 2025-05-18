# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Django port
EXPOSE 8000

# Run Django dev server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
