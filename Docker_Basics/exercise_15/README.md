# Exercise 15 – Running Containers

## Objective
Learn how to run, manage, inspect, stop, and remove Docker containers.

## Containers Used

### Ubuntu
Ubuntu is a Linux operating system commonly used for servers and development environments.

Command:

```bash
docker run -it ubuntu

### Check container status

Command 

```bash
docker ps -a | head
```

### Alpine
Alpine is a lightweight Linux distribution used for small and efficient Docker images.

### Command 

```bash
docker run -it alpine
```

### Nginx
Nginx is a web server used to serve websites and applications.

### Command

```bash
docker run -d --name my-nginx nginx
```
### List running containers

## Command

```bash
docker ps
```

### List all containers


### Command

```bash
docker ps -a
```


### Stop Containers: For example you want to stop nginx

```bash
docker stop my-nginx
```
### Remove containers

##Command

```bash
docker rm my-nginx
```

### Inspect containers

##Command

```bash
docker inspect my-nginx
```
