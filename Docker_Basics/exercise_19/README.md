# Exercise 19 – Dockerfile

## Overview

This exercise focused on creating a custom Docker image for a simple Python application using a Dockerfile. Unlike previous exercises where pre-built images were downloaded from Docker Hub, this exercise demonstrated how to package an application into a reusable Docker image.

The exercise covered the complete image creation workflow, including writing a Dockerfile, building an image, running a container, modifying the application, and rebuilding the image to apply changes.

---

## Objectives

- Create a simple Python application.
- Write a Dockerfile.
- Build a Docker image.
- Run a container from the image.
- Modify the application source code.
- Rebuild the Docker image.
- Verify that the updated application runs correctly.



## Dockerfile Used

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY hello.py .

CMD ["python", "hello.py"]
```

---

## Python Application

Initial version:

```python
print("Hello from Docker!")
```

Modified version:

```python
print("Docker images are rebuilt after code changes!")
```

---

## Commands Used

### Build the Docker Image

```bash
docker build -t exercise19-python .
```

### List Docker Images

```bash
docker images
```

### Run the Container

```bash
docker run --name hello-container exercise19-python
```

### View Containers

```bash
docker ps -a
```

### Remove the Container

```bash
docker rm hello-container
```

### Rebuild the Image After Code Changes

```bash
docker build -t exercise19-python .
```

---

## Expected Outputs

First execution:

```
Hello from Docker!
```

After modifying the application and rebuilding:

```
Docker images are rebuilt after code changes!
```

---

## Key Concepts Learned

- A Dockerfile is a blueprint for creating Docker images.
- `FROM` specifies the base image.
- `WORKDIR` sets the working directory inside the image.
- `COPY` copies files from the host into the image.
- `CMD` defines the default command executed when a container starts.
- Docker images must be rebuilt whenever application source code changes.
- Containers always run the version of the application stored inside the image.

---

## Conclusion

This exercise introduced the process of building custom Docker images using a Dockerfile. It demonstrated how Docker packages an application together with its runtime environment, ensuring consistent execution across different systems. By modifying the application and rebuilding the image, the exercise reinforced the importance of image rebuilding whenever changes are made to the application source code.
