# Use Python 3.10
FROM python:3.10

# Install required packages
RUN apt-get update && apt-get install -y nginx

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy nginx configuration
COPY nginx.conf /etc/nginx/sites-enabled/default

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 80
EXPOSE 80

# Start Nginx and Gunicorn
CMD service nginx start && gunicorn Ananta_Devgad_Hapus.wsgi:application --bind 0.0.0.0:8000
