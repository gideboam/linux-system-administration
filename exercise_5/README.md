### Exercise 5 - Process Management

# Exercise 5 – Process Management

## Objective

The goal of this exercise was to learn how Linux manages running processes and to practice common process management tasks performed by Linux administrators, DevOps engineers, Site Reliability Engineers (SREs), and Data Engineers.

## Tasks Completed

* Started multiple background processes.
* Viewed running processes.
* Found a process by name.
* Terminated a running process using its Process ID (PID).
* Restarted a process.
* Monitored CPU and system resource usage.

## Commands Used

### Start Background Processes

```bash
sleep 300 &
sleep 1000 &
sleep 10000 &
```

The `sleep` command creates a process that waits for a specified number of seconds. The `&` symbol runs the process in the background, allowing the terminal to remain available for additional commands.

### View Running Processes

```bash
ps
```

Displays the processes associated with the current terminal session.

```bash
ps aux
```

Displays all running processes on the system with detailed information, including the process owner, CPU usage, memory usage, Process ID (PID), and command.

### Find a Process by Name

```bash
ps aux | grep '[s]leep'
```

Searches for running processes with the name `sleep`. Using `[s]leep` prevents the `grep` command from matching itself in the output.

### Stop a Process

```bash
kill <PID>
```

Example:

```bash
kill 1126854
```

Terminates the process identified by the specified Process ID (PID).

### Restart a Process

```bash
sleep 10000 &
```

After terminating the previous process, a new `sleep` process was started. Linux assigned it a new PID because every running process has a unique Process ID.

### Monitor CPU and Memory Usage

```bash
top
```

Displays real-time information about system performance, including CPU utilization, memory usage, running processes, and system load.

Press `q` to exit the `top` interface.

## Key Concepts Learned

* A **program** is an application stored on disk, while a **process** is a program currently running in memory.
* Every running process is assigned a unique **Process ID (PID)** by the Linux kernel.
* Background processes allow users to continue working in the terminal while commands execute.
* The `ps` command provides a snapshot of running processes.
* The `grep` command can be combined with `ps aux` to locate specific processes.
* The `kill` command terminates a process using its PID.
* Restarting a process creates a new process with a new PID.
* The `top` command is used to monitor system performance and identify processes consuming significant CPU or memory resources.

## Outcome

This exercise provided practical experience in Linux process management, including creating, locating, terminating, restarting, and monitoring processes. These skills are essential for managing Linux servers and troubleshooting applications in DevOps, Data Engineering, and Site Reliability Engineering environments.
