# Use an official lightweight Python image
FROM python:3.10-slim

# Install system dependencies required for OpenCV and Mediapipe
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /code

# Copy requirements first to leverage Docker caching
COPY ./requirements.txt /code/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the rest of your application code
COPY . .

# Hugging Face Spaces strictly requires port 7860
EXPOSE 7860

# Run the FastAPI app using uvicorn on port 7860
CMD ["uvicorn", "main.py:app", "--host", "0.0.0.0", "--port", "7860"]
