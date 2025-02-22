# Use slim version of Python for a smaller image
FROM python:3.10-slim

# Set environment variables to prevent .pyc files and enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /app/

# Ensure persistent storage for SQLite
RUN mkdir -p /persistent-data
ENV SQLITE_PATH=/persistent-data/db.sqlite3

# Expose port 8000 for Django
EXPOSE 8000

# Run migrations and start the app
CMD ["sh", "-c", "python manage.py migrate && gunicorn --bind 0.0.0.0:8000 budget_tracker.wsgi:application"]
