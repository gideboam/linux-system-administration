
# Exercise 2 - File Management

## Objective

The onjective of this exercise is to learn basic linux file management commands by creating directories, creating files, copying files, moving files, deleting files and renaming files. 

# Commands Used

### 1. Create the Directory Structure

```bash
mkdir -p ~/training/{data,logs,scripts,backup}
```

### Explanation

- `mkdir` means **make directory**.
- The `-p` option tells Linux to create the parent directory if it does not already exist.
- The `~` symbol represents the current user's home directory.
- Brace expansion `{data,logs,scripts,backup}` creates four directories with one command instead of typing four separate commands.

This command creates the following directory structure:

```text
training/
├── data/
├── logs/
├── scripts/
└── backup/
```

---

## 2. Create Five Empty CSV Files

### Command

```bash
touch sensor1.csv sensor2.csv sensor3.csv sensor4.csv sensor5.csv
```

### Explanation

- `touch` creates empty files if they do not already exist.
- If the files already exist, it updates their modification timestamp.
- Five CSV files are created with a single command.

---

## 3. Copy the CSV Files to the Backup Directory

### Command

```bash
cp *.csv ../backup/
```

### Explanation

- `cp` means **copy**.
- `*.csv` is a wildcard that represents every file ending with `.csv`.
- `..` means go up one directory.
- `backup/` is the destination directory.

The original files remain in the `data` directory while copies are created in the `backup` directory.

---

## 4. Move One File into the Logs Directory

### Command

```bash
mv sensor1.csv ../logs/
```

### Explanation

- `mv` means **move**.
- This command transfers `sensor1.csv` from the `data` directory to the `logs` directory.
- Unlike `cp`, the original file is removed from the source directory after being moved.

---

## 5. Delete Two Files

### Command

```bash
rm sensor2.csv sensor3.csv
```

### Explanation

- `rm` means **remove**.
- It permanently deletes the specified files.
- Deleted files are generally not sent to a recycle bin in Linux.

---

## 6. Rename a File

### Command

```bash
mv sensor4.csv sensor_temperature.csv
```

### Explanation

The `mv` command can also rename files.

When the destination is another filename within the same directory, Linux changes the file's name instead of moving it to another location.

---

# Conclusion

This exercise introduced the fundamental file management commands used in Linux. I learned how to create directories, navigate between directories, create empty files, verify file locations, copy files, move files, delete files, and rename files. These commands are essential for managing files efficiently in a Linux environment and form the foundation for more advanced Linux system administration tasks.
