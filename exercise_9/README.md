# Exercise 9 – Commit History

## Overview

This exercise focuses on understanding Git commit history and the importance of making small, meaningful commits during software development. The objective is to practice creating project files, committing each logical change separately, and viewing the repository's history using different Git log commands.

A well-structured commit history allows developers to track project progress, understand when changes were made, identify who made them, and revert to previous versions if necessary. This is an essential skill in software development, DevOps, and Data Engineering.

## Objectives

* Initialize and organize a project for version control.
* Create project files incrementally.
* Make a separate Git commit after each logical change.
* View commit history using different Git log commands.
* Understand the purpose of detailed, one-line, and graphical commit history.

## Project Structure

```text
exercise_9/
├── README.md
└── sensor-project/
    ├── README.md
    ├── etl.py
    ├── config.json
    └── Dockerfile
```

## Tasks Completed

* Created the Exercise 9 project structure.
* Added the `etl.py` file and committed it.
* Added the `config.json` file and committed it.
* Added the `Dockerfile` and committed it.
* Displayed the complete commit history using `git log`.
* Displayed the condensed commit history using `git log --oneline`.
* Displayed the graphical commit history using `git log --graph --oneline --all`.


## Conclusion

This exercise strengthened my understanding of Git version control by demonstrating the complete workflow of staging, committing, and reviewing project history. Maintaining a clean and meaningful commit history improves collaboration, simplifies code reviews, and makes software projects easier to maintain over time.
