# Use official Python 3.10 slim image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy project files into container
COPY . .

# Install Flask
RUN pip install --no-cache-dir flask

# Expose the port Flask uses
EXPOSE 3000

# Run the app
CMD ["python", "app.py"]
