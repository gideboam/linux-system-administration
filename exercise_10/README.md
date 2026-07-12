# Exercise 10 – Branching

## Overview

This exercise focuses on understanding Git branching, feature development, merging, and branch management. The main objective was to practice creating independent feature branches, making changes without affecting the main codebase, merging completed features back into the `main` branch, and deleting branches after successful integration.

Branching is a fundamental concept in modern software development because it allows multiple developers to work on different features simultaneously while keeping the main project stable. In professional environments, developers rarely make changes directly on the main branch. Instead, they create feature branches, test their changes, and merge them into the main branch after completion

## Branches Created

Two feature branches were created during this exercise:

### feature/docker

This branch was created to handle Docker-related changes. The purpose of this branch was to modify the Docker configuration independently from the main branch.

The Dockerfile was updated with Python container configuration:

```dockerfile
FROM python:3.11-slim

WORKDIR /app
```

These instructions define the base Docker image and the default working directory inside the container.

---

### feature/etl

This branch was created to handle ETL-related development. The purpose was to add functionality to the ETL script without affecting the stable main branch.

The ETL script was updated with basic pipeline stages:

* Starting the ETL process.
* Extracting data.
* Transforming data.
* Loading data.
* Completing the ETL process.

## Git Commands Practiced

### Creating a branch

```bash
git branch feature/docker
```

This command creates a new branch called `feature/docker`. A branch acts as an independent line of development where changes can be made without affecting other branches.

---

### Switching branches

```bash
git switch feature/docker
```

This command moves the working environment to the selected branch. Any changes made after switching will belong to that branch.

---

### Creating and switching to a branch

```bash
git switch -c feature/etl
```

The `-c` option creates a new branch and immediately switches to it. This is a shorter alternative to creating a branch and switching separately.

---

### Checking available branches

```bash
git branch
```

This command displays all available branches. The branch marked with an asterisk (`*`) represents the currently active branch.

---

### Staging changes

```bash
git add Dockerfile
```

This command moves the modified Dockerfile into the staging area, preparing it for a commit.

Similarly:

```bash
git add etl.py
```

was used to stage the ETL script changes.

---

### Creating commits

Docker changes were committed using:

```bash
git commit -m "Update Dockerfile for application setup"
```

ETL changes were committed using:

```bash
git commit -m "Add ETL pipeline implementation"
```

Commits create permanent snapshots of project changes and allow developers to track the history of development.

---

## Merging Branches

After completing development on both feature branches, the branches were merged into the main branch.

The Docker branch was merged using:

```bash
git merge feature/docker
```

This resulted in a fast-forward merge because the main branch had no additional commits after the feature branch was created. Git simply moved the main branch pointer forward to include the Docker changes.

The ETL branch was merged using:

```bash
git merge feature/etl
```

This created a merge commit because the main branch and ETL branch had different development histories that needed to be combined.

The merge process integrated both features into the main project, producing a complete version containing both Docker and ETL improvements.

## Viewing Branch History

The final Git history was displayed using:

```bash
git log --oneline --graph --all
```


The graph showed how the Docker and ETL branches developed independently before being merged back into the main branch.

## Deleting Merged Branches

After successful merging, the feature branches were removed:

```bash
git branch -d feature/docker
```

and:

```bash
git branch -d feature/etl
```

