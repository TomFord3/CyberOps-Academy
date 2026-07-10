# Lesson 2 Summary - Variables, User Input, and f-Strings

**Date:** July 9, 2026

---

# Lesson Objective

Learn how to store information using variables, collect user input, and display formatted output using f-strings while building a realistic cybersecurity incident report generator.

---

# Topics Covered

## Variables

Learned how to store information in variables.

Examples:

- IP Address
- Username
- Hostname
- Severity
- Alert
- Case ID
- Domain
- Timestamp

Variables allow information to be stored once and reused throughout the program, making code easier to read, maintain, and update.

---

## Strings

Learned that text values are stored as strings (`str`).

Examples:

```python
username = "Admin"
hostname = "WIN-WS001"
```

Even though an IP address contains numbers, it is typically stored as a string because it represents text rather than a value used for mathematical calculations.

---

## User Input

Introduced the `input()` function.

Example:

```python
username = input("Enter the username: ")
```

Instead of hardcoding values, the program now asks the user to enter information while it is running.

This makes the program interactive and reusable.

---

## f-Strings

Learned how to format output using f-strings.

Example:

```python
print(f"Username: {username}")
```

f-strings allow variables to be inserted directly into a string, making output cleaner and easier to read.

---

## Comments

Learned how to document Python code using comments.

Example:

```python
# Store incident information collected during a SOC investigation.
```

Comments should explain **why** the code exists rather than simply describing what the code does.

---

# Project Completed

## SOC Incident Report Generator

Created an interactive Python application that:

- Collects user input
- Stores values in variables
- Displays a formatted incident report

The application currently collects:

- Case ID
- Username
- Hostname
- IP Address
- Domain
- Timestamp
- Severity
- Alert Description

---

# Git Skills Reinforced

Practiced:

- Editing Python files
- Saving changes
- Running Python from the terminal
- Creating Git commits
- Pushing updates to GitHub

Began becoming more comfortable using Git without step-by-step guidance.

---

# Cybersecurity Connections

This lesson directly relates to Security Operations Center (SOC) workflows.

Incident response tools commonly collect:

- IP Addresses
- Usernames
- Hostnames
- Severity Levels
- Case IDs
- Alert Information

Python variables provide a structured way to organize and process this information before it is analyzed, stored, or exported.

Future versions of this project may include:

- Input validation
- Threat intelligence lookups
- Database storage
- PDF report generation
- AI-generated incident summaries

---

# Skills Learned

- Python Variables
- Strings
- User Input (`input()`)
- Formatted Strings (f-strings)
- Comments
- Basic Program Structure
- Terminal Execution
- Git Workflow

---

# Biggest Takeaways

- Variables store information that can be reused throughout a program.
- `input()` allows programs to collect information from the user instead of relying on hardcoded values.
- f-strings make output easier to read and maintain.
- Well-organized code with comments improves readability and future maintenance.
- Cybersecurity scripts often rely on variables to organize investigation data.

---

# Real-World Applications

These concepts can be applied to:

- SOC Incident Reporting
- Security Automation
- Log Collection
- Threat Hunting Scripts
- Investigation Tools
- Detection Engineering
- API Integrations

---

# Career Connection

## Skills Practiced

- Python Fundamentals
- Git
- Documentation
- Problem Solving
- Cybersecurity Automation

## Interview Question

**What is a variable, and why are variables important?**

**Answer:**

A variable stores information that can be reused throughout a program. Variables improve readability, reduce duplicate code, and make programs easier to maintain because values only need to be updated in one location.

---

# Milestones Completed

✅ Created first interactive Python program

✅ Used variables to store investigation data

✅ Learned the `input()` function

✅ Used f-strings for formatted output

✅ Improved code documentation

✅ Executed Python from the terminal

✅ Successfully committed project updates to GitHub

---

# Vocabulary Learned

| Term | Definition |
|------|------------|
| Variable | A named location that stores a value. |
| String (`str`) | A sequence of text characters. |
| `input()` | Collects input from the user during program execution. |
| f-string | A formatted string that allows variables to be embedded directly inside text using `{}`. |
| Comment | Non-executable notes used to explain code. |

---

# Confidence Rating

Git: ⭐⭐⭐⭐☆

GitHub: ⭐⭐⭐⭐☆

Variables: ⭐⭐⭐⭐⭐

User Input: ⭐⭐⭐⭐☆

f-Strings: ⭐⭐⭐⭐☆

Overall Confidence: ⭐⭐⭐⭐☆

---

# Next Lesson Preview

Lesson 3 – Data Types & Networking Fundamentals

Topics include:

- Data Types
- Integers
- Floats
- Booleans
- Type Conversion
- IP Addresses
- Ports
- Networking Fundamentals

Project:

Network Alert Data Checker

---

# Personal Reflection

Today's lesson was the first time I created an interactive Python program. Instead of hardcoding values, I learned how to prompt the user for information using the `input()` function. I also learned how variables organize data and how f-strings create clean, professional output. As someone with SOC experience, I immediately recognized how these concepts could be applied to incident reporting and automation. I also started thinking ahead about improvements such as input validation, database storage, and AI integration, which showed me that learning Python is not just about syntax—it's about solving real cybersecurity problems.