 # Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire current directory into the container at /app
COPY . /app

# Expose the port that Streamlit runs on
EXPOSE 

# Command to run the Streamlit app
CMD ["streamlit", "run", "App.py"]

