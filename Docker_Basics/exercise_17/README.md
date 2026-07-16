# Exercise 17 – Docker Volumes

## Overview

This exercise focused on understanding **Docker volumes** and their role in providing persistent storage for Docker containers. The primary objective was to create a Docker volume, attach it to a PostgreSQL container, and verify that database data remains intact even after the container is removed and recreated.

Docker volumes are essential for stateful applications such as databases because they store data outside the container's writable layer. This ensures that important data is preserved independently of the container's lifecycle.

---

## Objectives

* Understand the purpose of Docker volumes.
* Create and manage Docker volumes.
* Run a PostgreSQL container using a Docker volume.
* Store data inside the PostgreSQL database.
* Verify that data persists after deleting and recreating the container.

---

## Prerequisites

* Docker installed and running
* Basic understanding of Docker containers and images
* PostgreSQL Docker image (`postgres:15`)

---

## Tasks Performed

### 1. Listed Existing Docker Volumes

Displayed all Docker volumes available on the host system.

```bash
docker volume ls
```

---

### 2. Created a Docker Volume

Created a dedicated volume to store PostgreSQL database files.

```bash
docker volume create postgres_data_ex17
```

---

### 3. Started a PostgreSQL Container Using the Volume

Launched a PostgreSQL 15 container and mounted the Docker volume to PostgreSQL's data directory.

```bash
docker run -d \
--name postgres_volume_ex17 \
-e POSTGRES_PASSWORD=password123 \
-v postgres_data_ex17:/var/lib/postgresql/data \
postgres:15
```

---

### 4. Verified the Running Container

Confirmed that the PostgreSQL container was running successfully.

```bash
docker ps
```

---

### 5. Connected to PostgreSQL

Accessed the PostgreSQL command-line interface inside the running container.

```bash
docker exec -it postgres_volume_ex17 psql -U postgres
```

---

### 6. Created a Sample Table

Created a table named **students**.

```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);
```

---

### 7. Inserted Sample Data

Inserted a sample record into the table.

```sql
INSERT INTO students (name)
VALUES ('Gideon');
```

---

### 8. Verified the Stored Data

Confirmed that the record had been successfully inserted.

```sql
SELECT * FROM students;
```

Expected output:

```text
 id |  name
----+---------
 1  | Gideon
```

---

### 9. Stopped and Removed the PostgreSQL Container

Stopped the running container and removed it without deleting the Docker volume.

```bash
docker stop postgres_volume_ex17
```

```bash
docker rm postgres_volume_ex17
```

---

### 10. Recreated the PostgreSQL Container

Started a new PostgreSQL container using the same Docker volume.

```bash
docker run -d \
--name postgres_volume_ex17_new \
-e POSTGRES_PASSWORD=password123 \
-v postgres_data_ex17:/var/lib/postgresql/data \
postgres:15
```

---

### 11. Verified Data Persistence

Connected to the new PostgreSQL container and confirmed that the previously inserted data still existed.

```bash
docker exec -it postgres_volume_ex17_new psql -U postgres
```

```sql
SELECT * FROM students;
```

The existing record confirmed that the Docker volume preserved the database data even after the original container had been removed.

---

## Key Concepts Learned

* Docker volumes provide persistent storage outside the container.
* Containers are temporary, while volumes are designed to survive container removal.
* Databases should store their data in Docker volumes to prevent data loss.
* Multiple containers can use the same volume over time.
* Docker volumes are a best practice for running stateful applications such as PostgreSQL, MySQL, MongoDB, and Redis.

---

## Commands Summary

| Command                                                                                                                                 | Purpose                                          |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| `docker volume ls`                                                                                                                      | List all Docker volumes                          |
| `docker volume create postgres_data_ex17`                                                                                               | Create a Docker volume                           |
| `docker run -d --name postgres_volume_ex17 -e POSTGRES_PASSWORD=password123 -v postgres_data_ex17:/var/lib/postgresql/data postgres:15` | Run PostgreSQL with a mounted volume             |
| `docker ps`                                                                                                                             | List running containers                          |
| `docker exec -it postgres_volume_ex17 psql -U postgres`                                                                                 | Access PostgreSQL                                |
| `CREATE TABLE students (...)`                                                                                                           | Create a database table                          |
| `INSERT INTO students (name) VALUES ('Gideon');`                                                                                        | Insert sample data                               |
| `SELECT * FROM students;`                                                                                                               | Verify stored data                               |
| `docker stop postgres_volume_ex17`                                                                                                      | Stop the PostgreSQL container                    |
| `docker rm postgres_volume_ex17`                                                                                                        | Remove the container                             |
| `docker run ... postgres_volume_ex17_new ...`                                                                                           | Create a new container using the existing volume |

---

## Conclusion

This exercise demonstrated the importance of Docker volumes in managing persistent application data. By creating a dedicated volume for PostgreSQL and verifying that the database remained intact after the original container was deleted, it became clear that Docker volumes provide reliable and persistent storage independent of a container's lifecycle. This concept is fundamental in DevOps, cloud computing, and containerized application deployment, where preserving data is critical for production systems.
