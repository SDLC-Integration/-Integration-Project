# Use Python 3.9 as the base image

FROM python:3.9
 
# Set working directory inside the container

WORKDIR /app
 
# Copy Python script to the container

COPY QR-Generator.py .
 
# Install dependencies

RUN pip install qrcode[pil]
 
# Define the command to run the script

CMD ["python", "qr_generator.py"]

 
