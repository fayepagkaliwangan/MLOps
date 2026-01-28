# Lecture 3 — Dockerizing a FastAPI Application

This project is a continuation of Lecture 2 and demonstrates how to containerize a simple FastAPI application using Docker, as part of the MLOps course.

The goal of this lecture is to show how an API can be packaged with its dependencies and run consistently across environments.

---

## Project Structure

- `main.py`  
  Contains the FastAPI application and API routes.

- `scoring.py`  
  Contains placeholder scoring logic used by the API.

- `requirements.txt`  
  Lists the Python dependencies required to run the application.

- `Dockerfile`  
  Defines how to build the Docker image for the API.

---

## Docker Instructions (Lecture 3)

### Build the Docker image

From inside the `2026-22-01_Lecture3` directory, run:

```bash
docker build -t lecture3-api .

### Run the container
docker run -p 8000:8000 lecture3-api
docker run -p 8001:8000 lecture3-api