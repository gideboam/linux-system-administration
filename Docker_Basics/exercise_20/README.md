# Exercise 20 – Docker Compose

## Overview

This exercise introduces **Docker Compose**, a tool used to define and manage multi-container Docker applications using a single YAML configuration file. Instead of creating and managing containers individually, Docker Compose allows multiple services to be deployed, started, stopped, and removed with a single command.

In this exercise, a Docker Compose configuration was created to deploy three services: PostgreSQL, Adminer, and Redis. The exercise also demonstrated how to manage the entire application stack using Docker Compose commands.

---

## Objectives

- Understand the purpose of Docker Compose.
- Create a `docker-compose.yml` file.
- Deploy multiple containers from a single configuration file.
- Configure environment variables for containers.
- Expose container ports to the host machine.
- Manage services using Docker Compose commands.
- Understand the automatically created Docker network.

---

## Technologies Used

- Docker
- Docker Compose
- PostgreSQL 15
- Adminer
- Redis
- YAML

---

## Services Deployed

### PostgreSQL

A PostgreSQL database server used to store application data.

### Adminer

A lightweight web-based database management tool used to connect to and manage the PostgreSQL database through a web browser.

### Redis

An in-memory data store commonly used for caching, session storage, and message brokering.

---

## Docker Compose File

The `docker-compose.yml` file defines:

- PostgreSQL service
- Adminer service
- Redis service
- Environment variables
- Port mappings
- Restart policies
- Default Docker network

Docker Compose automatically created a bridge network to allow all services to communicate with one another.

---

## Commands Performed

### Validate the Compose file

```bash
docker compose config
```

### Download required images

```bash
docker compose pull
```

### Start all services

```bash
docker compose up -d
```

### View running services

```bash
docker compose ps
```

### Stop all services

```bash
docker compose stop
```

### Start stopped services

```bash
docker compose start
```

### Restart all services

```bash
docker compose restart
```

### Remove all services and the network

```bash
docker compose down
```

---

## What I Learned

Through this exercise, I learned how Docker Compose simplifies the deployment and management of multi-container applications. Rather than starting each container individually, Docker Compose allows an entire application stack to be managed from a single YAML file.

I also learned how Docker Compose automatically creates a private network so containers can communicate securely using their service names.

Finally, I gained hands-on experience with the complete lifecycle of a Docker Compose application, including starting, stopping, restarting, inspecting, and removing services.

---

## Outcome

Successfully created and managed a multi-container application consisting of:

- PostgreSQL
- Adminer
- Redis

using Docker Compose and a single `docker-compose.yml` configuration file.
