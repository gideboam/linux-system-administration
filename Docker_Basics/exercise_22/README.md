# Exercise 22 – Docker Resource Limits

## Overview

This exercise demonstrates how Docker containers can be controlled using resource limits. In production environments, containers often share the same server resources, therefore it is important to prevent one container from consuming all available CPU and memory.

Docker provides resource management options that allow administrators to define how much CPU and RAM a container can use.

In this exercise, a Docker container was created with:

- A maximum CPU allocation of 1 CPU
- A maximum memory allocation of 512 MB RAM

The configured limits were then verified using Docker inspection and monitoring commands.

---

# Objectives

The objectives of this exercise were to:

- Create a container with CPU restrictions.
- Create a container with memory restrictions.
- Understand Docker resource management.
- Verify configured resource limits.
- Monitor container resource consumption.

---

# Creating the Resource-Limited Container

The following command was used:

```bash
docker run -d \
--name resource-test \
--cpus 1 \
-m 512m \
ubuntu \
sleep infinity
