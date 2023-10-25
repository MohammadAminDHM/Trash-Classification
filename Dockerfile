# Use an official Python runtime as the parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any needed Python packages specified in requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Allow for external connections
EXPOSE 8080

# Run the app when the container is started
CMD ["python", "app.py"]
