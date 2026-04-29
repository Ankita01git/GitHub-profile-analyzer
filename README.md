
# GitHub Profile Analyzer 🔍

A Python command-line app that fetches any GitHub user's profile and repositories using the GitHub API.

## Features
- 👤 Shows name, bio, location and followers
- 📦 Lists top 5 repositories sorted by stars
- 💻 Shows programming language of each repo
- 🔍 Filter repositories by language

## How to run

1. Install dependencies:
pip install requests

2. Run the app:
python github_analyzer.py

3. Enter any GitHub username when prompted
4. Optionally filter results by programming language

## Technologies used
- Python
- GitHub REST API
- requests library

## Example
Enter your Github username: torvalds
Filter by language? (press Enter to skip): C

Name: linux | Language: C | Stars: 187000
