# Exercise 7 – Linux Disk Management

## Objective

The objective of this exercise was to understand Linux disk management by monitoring storage usage, identifying large directories and files, checking filesystem capacity, and analyzing available inodes.

## Tasks Completed

### 1. Finding Largest Directories

The `du` (disk usage) command was used to identify directories consuming the most storage space.

Command:

```bash
du -h --max-depth=1 /
```

The `-h` option displays sizes in a human-readable format, while `--max-depth=1` limits the output to directories directly under the root directory.

The output was sorted to easily identify the largest directories:

```bash
du -h --max-depth=1 / | sort -hr
```

---

### 2. Finding Largest Files

The `find` command was used to locate large files on the system.

Command:

```bash
find / -type f -size +100M
```

Explanation

This helps identify files that may consume excessive disk space, such as large logs, backups, or datasets.

---

### 3. Checking Filesystem Usage

The `df` command was used to check disk capacity and available storage.

Command:

```bash
df -h
```


---

### 4. Checking Available Inodes

Linux uses inodes to store metadata about files, including ownership, permissions, and file locations.

Command:

```bash
df -i
```



Monitoring inode usage is important because a system can run out of inodes even when disk storage is still available.

