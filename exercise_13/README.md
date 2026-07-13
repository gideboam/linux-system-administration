# Exercise 13 – Ignore Files

## Overview

This exercise focuses on understanding how Git handles files that should not be tracked or uploaded to a remote repository. In real-world software development and Data Engineering projects, many files are created during development that should remain only on the local machine.

Examples include environment configuration files containing sensitive information, application log files, automatically generated Python cache files, and temporary files created during testing.

The main objective of this exercise was to learn how to configure Git to ignore specific files and directories using the `.gitignore` file. This helps keep repositories clean, prevents sensitive information from being exposed, and ensures that only important project files are stored in version control.

---

# Objectives

The objectives of this exercise were to:

- Understand the purpose of the `.gitignore` file.
- Create files and directories that should not be tracked by Git.
- Configure Git ignore rules.
- Verify that Git successfully ignores specified files.
- Commit `.gitignore` into the repository.
- Understand how ignored files are handled in professional development environments.

---

# Project Structure

The project structure created during this exercise was:

```
ignore-project/
│
├── .git/
│
├── .gitignore
│
├── .env
│
├── application.log
│
├── __pycache__/
│
└── temp/
```

---

# Initializing the Git Repository

The project was first initialized as a Git repository using:

```bash
git init
```

The `git init` command creates a hidden `.git` directory inside the project. This directory stores Git metadata such as commits, branches, and repository configuration.

Without the `.git` directory, Git cannot track changes or maintain project history.

---

# Creating Files to Ignore

Several files and directories were created to demonstrate Git ignore functionality.

## Creating Environment Configuration File

Command:

```bash
touch .env
```

The `.env` file is commonly used to store environment variables such as database credentials, API keys, and application settings.

Example:

```
DATABASE_PASSWORD=password123
API_KEY=abcdef
```

These files should not be uploaded to GitHub because they may contain sensitive information.

---

## Creating Log Files

Command:

```bash
touch application.log
```

Log files store application activity, errors, and debugging information.

Examples:

```
server.log
error.log
database.log
```

Since log files constantly change and can become very large, they are usually excluded from source control.

---

## Creating Python Cache Directory

Command:

```bash
mkdir __pycache__
```

The `__pycache__` directory is automatically created by Python when programs are executed.

It contains compiled Python files such as:

```
app.cpython-311.pyc
```

These files are generated automatically and are not required in a Git repository.

---

## Creating Temporary Directory

Command:

```bash
mkdir temp
```

Temporary directories usually contain testing files, temporary outputs, or intermediate data that should not be stored permanently.

---

# Creating the .gitignore File

The `.gitignore` file was created using:

```bash
touch .gitignore
```

The purpose of `.gitignore` is to provide instructions to Git about files and directories that should be ignored.

The following rules were added:

```
.env
*.log
__pycache__/
temp/
```

---

# Understanding .gitignore Rules

## Ignoring Environment Files

Rule:

```
.env
```

This tells Git to ignore the `.env` file.

This prevents sensitive information such as:

- Passwords
- API keys
- Database credentials

from accidentally being committed.

---

## Ignoring Log Files

Rule:

```
*.log
```

The wildcard character `*` represents any filename.

This rule ignores all files ending with `.log`.

Examples:

```
application.log
server.log
error.log
```

---

## Ignoring Python Cache Files

Rule:

```
__pycache__/
```

The `/` indicates that this is a directory.

This prevents Python-generated cache files from being tracked.

---

## Ignoring Temporary Files

Rule:

```
temp/
```

This prevents temporary directories and their contents from being added to Git.

---

# Verifying Ignored Files

The command:

```bash
git status
```

was used to check the repository status.

After creating `.gitignore`, Git only displayed:

```
.gitignore
```

because the other files were successfully ignored.

---

To specifically display ignored files, the command:

```bash
git status --ignored
```

was used.

The output confirmed:

```
Ignored files:

.env
application.log
```

This verified that Git was correctly applying the ignore rules.

---

# Committing .gitignore

The `.gitignore` file was added to Git using:

```bash
git add .gitignore
```

This moved the file into the staging area.

The changes were then saved permanently using:

```bash
git commit -m "Add gitignore configuration"
```

This created a commit containing the repository ignore configuration.

---

# Important Git Concept Learned

The `.gitignore` file does not delete files from the computer.

Instead, it tells Git:

> "Do not track these files or include them in commits."

For example:

```
.env
```

still exists on the server, but Git will ignore it.

---

# Real-World Application

In professional software engineering and Data Engineering environments, `.gitignore` is extremely important.

A typical Data Engineering project may contain:

```
data-pipeline/

├── extract.py
├── transform.py
├── load.py
├── .env
├── logs/
├── __pycache__/
└── temp/
```

A proper `.gitignore` file prevents unnecessary or sensitive files from being uploaded.

Common ignored files include:

- Environment variables.
- Password files.
- Application logs.
- Temporary data.
- Python cache files.
- Build artifacts.

---

# Skills Gained

By completing this exercise, I learned how to:

- Create and configure a `.gitignore` file.
- Prevent sensitive files from being committed.
- Ignore unnecessary generated files.
- Verify ignored files using Git commands.
- Maintain cleaner and safer Git repositories.

---

# Conclusion

Exercise 13 provided practical knowledge of Git file management and repository organization. Understanding `.gitignore` is an essential skill for developers, DevOps engineers, and Data Engineers because it helps protect sensitive information, reduces repository clutter, and ensures that only important project files are stored in version control.

Proper use of `.gitignore` is a standard practice in professional software development workflows.
