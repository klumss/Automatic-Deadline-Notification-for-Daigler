An automatic scheduled script that allows you get notified about your deadlines in Daigler25.

The script makes use of playwright to login and get data from your deadlines table in Daigler.
The username and password can be set in the .env.example file. Just replace the placeholders.

The script is scheduled to run every day at 5am (although github actions might delay it for an hour or two)
The schedule can be set in the main.yml file.

All dependencies are listed in pyproject.toml, I recommend using uv for setup.

NOTE: This project is not affiliated with Ateneo de Davao University. This is just a personal project of mine.
