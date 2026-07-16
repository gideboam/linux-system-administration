# Exercise 18 – Docker Networks

## Overview

This exercise focused on understanding Docker networking and how containers communicate with one another. A custom bridge network was created, and two containers—PostgreSQL and pgAdmin—were connected to it. Communication between the containers was verified using Docker's built-in networking and DNS capabilities.

Docker networks are essential when deploying multi-container applications because they provide secure and isolated communication between services without requiring manual IP address management.

---

## Objectives

* Understand the purpose of Docker networks.
* Create a custom bridge network.
* Run PostgreSQL and pgAdmin containers on the same network.
* Verify that both containers can communicate.
* Learn how Docker's internal DNS resolves container names.

---

## Prerequisites

* Docker installed and running
* PostgreSQL Docker image (`postgres:15`)
* pgAdmin Docker image (`dpage/pgadmin4`)

---

## Tasks Performed

### 1. Listed Existing Docker Networks

Displayed all Docker networks available on the system.

```bash
docker network ls
```

---

### 2. Created a Custom Bridge Network

Created a dedicated Docker bridge network for this exercise.

```bash
docker network create exercise18-network
```

---

### 3. Verified the Network

Confirmed that the newly created network existed.

```bash
docker network ls
```

---

### 4. Inspected the Network

Viewed detailed information about the custom network, including its subnet, gateway, driver, and connected containers.

```bash
docker network inspect exercise18-network
```

Initially, the `Containers` section was empty because no containers had been attached.

---

### 5. Started PostgreSQL on the Custom Network

Created a PostgreSQL container connected to the custom bridge network.

```bash
docker run -d \
--name postgres_ex18 \
--network exercise18-network \
-e POSTGRES_PASSWORD=password123 \
postgres:15
```

---

### 6. Started pgAdmin on the Same Network

Created a pgAdmin container and connected it to the same Docker network.

```bash
docker run -d \
--name pgadmin_ex18 \
--network exercise18-network \
-p 8080:80 \
-e PGADMIN_DEFAULT_EMAIL=admin@example.com \
-e PGADMIN_DEFAULT_PASSWORD=password123 \
dpage/pgadmin4
```

---

### 7. Verified Running Containers

Confirmed that both PostgreSQL and pgAdmin were running.

```bash
docker ps
```

---

### 8. Verified Network Membership

Inspected the custom network again and confirmed that both containers were connected.

```bash
docker network inspect exercise18-network
```

The output showed:

* `postgres_ex18`
* `pgadmin_ex18`

along with their assigned IP addresses.

---

### 9. Tested Communication Between Containers

Verified communication by pinging the PostgreSQL container from within the pgAdmin container.

```bash
docker exec -it pgadmin_ex18 ping -c 4 postgres_ex18
```

The successful replies confirmed that Docker's internal DNS resolved the container name and that both containers could communicate over the custom bridge network.

---

## Key Concepts Learned

* Docker networks enable communication between containers.
* A custom bridge network provides better organization and isolation than the default bridge network.
* Docker automatically assigns IP addresses to containers on a network.
* Docker includes an internal DNS service that allows containers to communicate using container names.
* Multi-container applications rely on Docker networking for secure and reliable communication.

---

## Commands Summary
                                                                                               
 Command                                                              Purpose        
 
 `docker network ls`                                                 List all Docker networks                
 `docker network create exercise18-network`                        Create a custom bridge network          
 `docker network inspect exercise18-network`                       View detailed network information       
 `docker run --network exercise18-network ... postgres:15`        Run PostgreSQL on the custom network    
 `docker run --network exercise18-network ... dpage/pgadmin4`     Run pgAdmin on the same network         
 `docker ps`                                                      Verify running containers               
 `docker exec -it pgadmin_ex18 ping -c 4 postgres_ex18`           Verify communication between containers 

---

## Conclusion

This exercise demonstrated how Docker networks allow multiple containers to communicate securely and efficiently. By creating a custom bridge network and attaching both PostgreSQL and pgAdmin to it, communication between the services was established without manually configuring IP addresses. Docker's built-in DNS resolved the PostgreSQL container by its name, illustrating a key feature used in real-world containerized applications. Understanding Docker networking is essential for building scalable, maintainable, and production-ready multi-container environments.
