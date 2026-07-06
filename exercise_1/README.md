# Exercise 1 - System Information

## Objective
The objective of this exercise is to learn how to inspect a linux server by displaying important system information.

# Exercise 1 - System Information

## OS Version

### Command:

```bash
cat /etc/os-release
```

### Explanation

This command displays information about the installed Linux operating system, including its name, version and other details.

## Display the kernel version

### Command:

```bash
uname -r
```

### Explanation

This command displays system information such linux kernel version


## Display CPU information

### Command:

```bash 
lscpu
```

### Explanation

This command shows detailed information about the CPU, such as the numebr of cores, archictecture, speed and the processor type.

## Display Memory Usage

### Command:

```bash
free -h
```

### Explanation

This command shows how the memory (RAM) is being used. It displays totat memory, used memory and available memory in a human-readable format

## Display disk usage

### Command:

```bash
df -h
```

### Explanation

This command shows the storage usage

## Display Uptime

### Command:

```bash
uptime
```

### Explanation

This command shows the current time, how long the server has been running, the number of logged in users and the system load averages.

## Display Hostname

### command:

```bash
hostname
```

### Explanation

This command shows the unique name assigned to a computer or server on a network

## Display logged-in users

### Command:

```bash
who
```

### Explanation

This command shows who is logged in, when they logged in and which terminal are they using.

## Display IP Address

### Command:
```bash
ip addr
```
### Explanation

This command displays the IP addresses assigned to the server network interfaces.  
