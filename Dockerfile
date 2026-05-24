FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create a startup script
RUN echo '#!/bin/bash\n\
echo "Starting Naqal AI..."\n\
echo "Listening on port ${PORT:-8080}"\n\
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080} --timeout-keep-alive 300\n\
' > /start.sh && chmod +x /start.sh

CMD ["/start.sh"]
