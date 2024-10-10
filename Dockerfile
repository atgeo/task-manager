# Use the official Python image from the Docker Hub
FROM python:3.13

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements file into the container at /app
COPY requirements.txt ./

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN echo "DEBUG=on" >> .env && \
    echo "SECRET_KEY=mysecretkey" >> .env

# Copy the entire application code into the container
COPY . .

# Expose Django’s default port
EXPOSE 8000

# Run the Django development server on all network interfaces
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
