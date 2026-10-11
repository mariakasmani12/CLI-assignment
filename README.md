# GitHub Profile CLI

## Description
This Python program fetches GitHub profile information for multiple usernames using the GitHub API.

## Requirements
- Python 3
- Requests library

## Installation
Install the required library by running:

```bash
pip install requests
```

## How to Run
Run the program in the terminal:

```bash
python main.py
```

Enter GitHub usernames separated by commas.

Example:

```text
octocat,torvalds,mariakasmani12
```

## Features
- Accepts multiple GitHub usernames in one run.
- Saves user information in `summary.csv`.
- Retries failed requests up to 3 times.
- Logs errors in `errors.log`.

## CSV Output
The `summary.csv` file contains these columns:

- login
- name
- public repos
- followers

## Example Output

```text
Success: octocat
Success: torvalds
Finished! Check summary.csv and errors.log
```

The actual output depends on the API response.
