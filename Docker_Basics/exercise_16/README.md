# Exercise 16 – Docker Images

## Objective

The objective of this exercise was to understand what Docker images are and how they are managed. The exercise focused on downloading images from Docker Hub, listing available images, inspecting image metadata, and removing images that were no longer needed.

---

## What is a Docker Image?

A Docker image is a **read-only template** that contains everything needed to create and run a Docker container. It includes the application code, dependencies, libraries, configuration files, and instructions required to start the application.


---

## Images Used

### Ubuntu

Ubuntu is a popular Linux distribution widely used for servers and application development. The Ubuntu image provides a complete Linux environment inside a Docker container.

Command used:

```bash
docker pull ubuntu
```

---

### PostgreSQL

PostgreSQL is a powerful open-source relational database management system used to store structured data.

Command used:

```bash
docker pull postgres
```

---

### Redis

Redis is a high-performance in-memory data store commonly used for caching, session management, and real-time applications.

Command used:

```bash
docker pull redis
```

---

## Commands Practiced

### List all Docker images

```bash
docker images
```

Displays every Docker image stored locally.

---

### Download an image

```bash
docker pull <image_name>
```

Downloads an image from Docker Hub if it is not already available locally.

Examples:

```bash
docker pull ubuntu
docker pull postgres
docker pull redis
```

---

### Inspect an image

```bash
docker image inspect ubuntu
```

Displays detailed information about an image, including its ID, operating system, architecture, environment variables, layers, and creation date.

---

### Remove an image

```bash
docker rmi redis
```

or

```bash
docker image rm redis
```

Removes a Docker image from the local machine. Docker will prevent the removal of images that are still being used by existing containers unless those containers are removed first.

---

## Key Learning Points

- Docker images are templates used to create containers.
- A single image can create multiple containers.
- Images are downloaded from Docker Hub using `docker pull`.
- `docker images` lists all locally available images.
- `docker image inspect` provides detailed metadata about an image.
- `docker rmi` removes images that are no longer required.
- Docker protects images that are still being used by containers.

---

## Conclusion

This exercise introduced the fundamentals of Docker image management. By learning how to download, inspect, list, and remove images, I gained a better understanding of the relationship between Docker images and containers. These skills provide the foundation for building, deploying, and managing containerized applications in future Docker and DevOps projects.
