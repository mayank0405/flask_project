FROM python:3.9.19-slim

WORKDIR /flask_project

# Copy and install dependencies in one step to leverage Docker caching
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variables for Flask
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

# Use CMD instead of ENTRYPOINT for flexibility
CMD ["flask", "run"]
