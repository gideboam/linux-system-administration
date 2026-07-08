# Exercise 4 - Searching Files

## Objectives

The objective of this exercise was to learn how to search for files in Linux using the find and grep commands.

### Create multiple log files

## Command used

```bash
touch app.log system.log auth.log database.log server.log
```
### Add content to a file

## Command used 

```bash
echo "INFO: User log in succesful" > auth.log
```

### Find files larger 50M

## Command used

```bash
find . -size +50M
```
The output was nothing so I created a realistic large file using the command 

```bash
dd if = /dev/zero of = large_file.log bs=1M count=60
```
This created a realistic larger file so when we run the command to search for files larger than 50M, the output was large_file.log

### Find files modified today

## Command used

```bash
find . -mtime -1
```

### Find files ending with .csv

I created multiple files with some ending with .csv

## Command used 

```bash
find . -name "*.csv
```
This command listed files ending with .csv

### Search for the world ERROR inside logs

## Command used

```bash
grep "ERROR" *.log
```
