# Exercise 14 – Install Docker

## Objective

The objective of this exercise was to verify that Docker was correctly installed and working or actively running. 

## Tasks Completed

- Verified the installed Docker version.
- Verified communication with the Docker daemon.
- Verified the Docker service status.
- Verified Docker socket permissions.
- Confirmed user membership in the `docker` group.

## Commands Used

```bash
docker --version
docker info
docker ps
systemctl status docker
groups
ls -l /var/run/docker.sock
```
