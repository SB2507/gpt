# Use the official Python image as the base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the Streamlit app files into the container
COPY app

# Expose the port your Streamlit app runs on
EXPOSE 8501

# Set the environment variable to ensure that Python outputs everything
# directly to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# Command to run your Streamlit app
CMD ["streamlit", "run", "app/App.py"]
