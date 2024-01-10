FROM python:3.9-bullseye

# Set the working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt requirements.txt

# Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy local code to container
COPY . .

# Expose port 
EXPOSE 8501

# default command
CMD ["streamlit", "run", "app.py"]