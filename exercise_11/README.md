# Exercise 11 – Undo Mistakes

## Overview

This exercise focuses on learning how to recover from common mistakes in Git. During software development, developers frequently make accidental commits, stage the wrong files, delete important files, or need to inspect changes before committing. Git provides several powerful commands to safely recover from these situations without losing work.

The objective of this exercise is to practice undoing commits, restoring deleted files, unstaging files, and viewing file differences before committing.

## Git Commands Practiced

### Initialize Repository

```bash
git init
```

Creates a new Git repository.

---

### Check Repository Status

```bash
git status
```

Displays the current state of the repository, including staged, unstaged, and untracked files.

---

### View Commit History

```bash
git log --oneline
```

Displays a simplified commit history.

---

### Undo the Last Commit

```bash
git reset --soft HEAD~1
```

Removes the most recent commit while keeping all changes staged for recommitting.

---

### Restore a Deleted File

```bash
git restore app.py
```

Restores a deleted tracked file from the latest commit.

---

### Unstage a File

```bash
git restore --staged config.json
```

Removes a file from the staging area while keeping it in the working directory.

---

### View File Differences

```bash
git diff
```

Displays the differences between the current working directory and the latest committed version of tracked files.

---

## Skills Gained

By completing this exercise, I learned how to:

- Recover from accidental commits.
- Restore deleted files without losing data.
- Remove mistakenly staged files.
- Review changes before committing.
- Interpret Git status messages.
- Use Git recovery commands safely and effectively.
