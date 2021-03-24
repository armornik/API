# Finding user data with API GitHub


This web service allows you to find out in which projects a specific GitHub user made pull requests from them.

On the main page, you must enter the user's nickname on the GitHub, and click “Send”.
As a result, you will see a page with a list of projects to which the user made a pull request and was smerged. For each project, you will see:
- the title of the project;
- link to the project on GitHub;
- number of stars on GitHub;
- links to merged pull requests from the user;
- links to non-merged pull request from user;
- for each pull request, you will see the number of comments in this pull request.


## Installation

1. Clone repository.
2. Create virtual environment.
3. install requirements `pip install -r requirements.txt`
4. Create your .env file:
- in the same directory as settings.py, create a file called ‘.env’;
- declare your environment variables in .env (make sure you don’t use quotations around strings):
  SECRET_KEY=qwerty1234567890qwerty1234567890
  GITHUB_TOKEN=qwerty1234567890qwerty1234567890
  # IMPORTANT: Add your .env file to .gitignore
5. Add in settings.py:
import environ
env = environ.Env()
environ.Env.read_env()
GITHUB_TOKEN = env('GITHUB_TOKEN')
6. Replace your environment variables in settings.py:
SECRET_KEY = env('SECRET_KEY')
  