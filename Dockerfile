
# Use the official Python image as the base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt   # Change to include --no-cache-dir flag to avoid caching issues

# Copy the Flask app files into the container
COPY app app

# Expose the port your Flask app runs on
EXPOSE 5000

# Set the environment variable to ensure that Python outputs everything
# directly to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# Set the Flask environment variable to 'production'
ENV FLASK_ENV=production

# Command to run your Flask app
CMD ["python", "app/App.py"]
