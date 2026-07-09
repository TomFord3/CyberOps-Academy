# Lesson 1 Summary - Development Environment & Git Foundations

**Date:** July 8, 2026

---

# Lesson Objective

Build a professional development environment and learn the fundamentals of Git and GitHub so future Python, PowerShell, and cybersecurity projects can be version controlled and documented.

---

# Topics Covered

## Development Environment

Installed and configured:

- Git
- Visual Studio Code
- Python
- PowerShell (verified)
- GitHub

---

## Git Configuration

Configured Git with:

- Global username
- Global email address

Verified Git installation using:

```powershell
git --version
```

Verified Python installation using:

```powershell
python --version
```

Verified VS Code installation using:

```powershell
code --version
```

---

# GitHub

Created my first public repository:

**CyberOps-Academy**

Purpose:

Document my journey learning:

- Python
- PowerShell
- AI
- Cybersecurity
- Security Automation
- Detection Engineering
- Threat Hunting

---

# Repository Structure

Created the following structure:

```text
CyberOps-Academy
│
├── AI
├── CheatSheets
├── Labs
├── Lessons
│   └── 01-Environment
│       ├── notes.md
│       ├── summary.md
│       ├── quiz.md
│       └── reflections.md
│
├── PowerShell
├── Projects
├── Python
├── Resources
└── README.md
```

---

# Git Concepts Learned

## Repository

A repository is the project Git manages.

---

## Working Directory

Where files are actively edited.

---

## Staging Area

Files prepared for the next commit.

---

## Commit

A snapshot of the staged files.

---

## GitHub

A remote copy of the Git repository used for backup, collaboration, and portfolio management.

---

# Git Workflow

```text
Create File
      ↓
git status
      ↓
Untracked
      ↓
git add .
      ↓
Staged
      ↓
git commit
      ↓
Snapshot Saved
      ↓
git push
      ↓
GitHub
```

---

# Commands Learned

```bash
git --version
```

Check Git installation.

---

```bash
git status
```

Shows repository status.

---

```bash
git add .
```

Stages all changes.

---

```bash
git commit -m "message"
```

Creates a snapshot.

---

```bash
git push
```

Uploads commits to GitHub.

---

```bash
git init
```

Creates a Git repository.

---

```bash
git config --global user.name
```

Displays the configured Git username.

---

```bash
git config --global user.email
```

Displays the configured Git email.

---

# Biggest Takeaways

Git does **not** automatically save files.

Git only tracks files that are staged.

Every commit is a permanent snapshot in the project's history.

GitHub stores the history of the project, not just the current files.

Documentation is just as important as writing code.

---

# Cybersecurity Connections

Version control is commonly used to manage:

- Python automation scripts
- PowerShell scripts
- Sigma detection rules
- YARA rules
- Security documentation
- Incident response playbooks
- Infrastructure-as-Code
- Detection engineering content

Proper version control allows teams to:

- Track changes
- Roll back mistakes
- Audit modifications
- Collaborate safely

---

# Skills Learned

- Git Fundamentals
- GitHub Fundamentals
- VS Code Navigation
- Development Environment Setup
- Markdown Basics
- Repository Organization
- Basic Documentation

---

# Milestones Completed

✅ Installed Git

✅ Installed Python

✅ Installed Visual Studio Code

✅ Configured Git

✅ Created first GitHub repository

✅ Created first Git commit

✅ Pushed first commit to GitHub

---

# Confidence Rating

Git: ⭐⭐⭐☆☆

GitHub: ⭐⭐⭐☆☆

VS Code: ⭐⭐⭐⭐☆

Python Installation: ⭐⭐⭐⭐☆

Overall Confidence: ⭐⭐⭐☆☆

---

# Next Lesson Preview

Lesson 2 - Python Variables

Topics:

- Variables
- Strings
- Printing
- Comments
- f-Strings

Project:

SOC Ticket #0001

Create an Incident Report Generator using Python.

---

# Personal Reflection

Today, I learned that Git is not just a backup tool. It is a version control system that tracks the history of a project through commits. Understanding the workflow of Working Directory → Staging Area → Commit helped me understand why Git requires multiple steps before changes are saved. I can also relate to this. Incase something breaks or another developer needs a specific file from the repository, they can see the changes that were made since the last commit to be able to change or fix the file. I also learned the importance of organizing projects from the beginning instead of creating random files and folders. This repository will serve as both my learning journal and my professional cybersecurity portfolio.