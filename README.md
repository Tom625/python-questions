# Python Challenges: 12 Weeks

## Overview
Welcome to the **Python Challenges: 12 Weeks** repository! This project is designed to help Python learners practice their skills through a series of challenges. The repository consists of **12 weeks of challenges**, each with **5+ questions**.

Each user solves the challenges by creating their own branch and submitting their solutions to their personal folder in the repository.

---

## How to Participate

### Step 1: Clone the Repository
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Tom625/python-questions.git
   ```
2. Navigate into the project directory:
   ```bash
   cd python-questions
   ```

---

### Step 2: Create Your Personal Folder
1. Inside the root directory, navigate to the `solutions/` folder:
   ```bash
   cd solutions/
   ```
2. Create a new folder with your GitHub username:
   ```bash
   mkdir <your-username>
   ```
   Example:
   ```
   mkdir solutions/janedoe
   ```

3. Copy the weekly challenge folders (`week1`, `week2`, etc.) into your personal folder:
   ```bash
   cp -r ../week* <your-username>/
   ```

   Example:
   ```
   cp -r ../week1 ../week2 ../week3 ... ../week12 solutions/janedoe/
   ```

   Your folder structure will look like this:
   ```
   solutions/janedoe/week1/question1.py
   solutions/janedoe/week2/question1.py
   ```

---

### Step 3: Create a Branch for Your Work
1. Create a new branch with your name:
   ```bash
   git checkout -b <your-username>
   ```
   Example:
   ```
   git checkout -b janedoe
   ```

---

### Step 4: Solve the Challenges
1. Open the `.py` files for the week you’re working on, and add your solutions below the questions written as comments.

Example:
`solutions/janedoe/week1/question1.py`:
```python
# Week 1, Question 1: Calculate the Sum of a List
# Difficulty: Beginner
#
# Write a function `sum_list(lst)` that takes a list of integers
# and returns the sum of all the integers.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: 10
#
# Your Solution:
def sum_list(lst):
    return sum(lst)
```

2. Save your changes.

---

### Step 5: Commit and Push Your Work
1. Stage and commit your changes:
   ```bash
   git add solutions/<your-username>
   git commit -m "Added solutions for week 1 by <your-username>"
   ```

2. Push your branch to the repository:
   ```bash
   git push origin <your-username>
   ```
   Example:
   ```bash
   git push origin janedoe
   ```

---

### Step 6: Open a Pull Request
1. Go to the repository on GitHub.
2. Click **Pull Requests** > **New Pull Request**.
3. Select your branch (`<your-username>`) as the source and `main` as the target.
4. Submit your pull request with a short description of the changes.

---

### Step 7: Review and Merge
- Your pull request will be reviewed, and feedback may be provided.
- Once approved, your branch will be merged into the `main` branch.

---

## Folder Structure
The repository is organized as follows:
```
python-questions/
├── week1/                      # Challenge templates for Week 1
│   ├── question1.py
│   ├── question2.py
│   └── ...
├── week2/                      # Challenge templates for Week 2
│   ├── question1.py
│   ├── question2.py
│   └── ...
├── ...
├── week12/                     # Challenge templates for Week 12
│   ├── question1.py
│   ├── question2.py
│   └── ...
├── solutions/                  # Directory for user submissions
│   ├── username1/              # Solutions by User 1
│   │   ├── week1/
│   │   └── week2/
│   ├── username2/              # Solutions by User 2
│   │   ├── week1/
│   │   └── week2/
│   └── ...
└── README.md
```

---

## Guidelines
- **Do Not Edit Others’ Files**: Only modify files in your personal folder (`solutions/<your-username>`).
- **Keep Your Branch Updated**: Before pushing new changes, always pull the latest `main` branch to avoid conflicts:
  ```bash
  git pull origin main
  git merge main
  ```
- **Submit a Pull Request**: Once you’re done solving challenges, submit a pull request for review.

---

Happy coding!

