# Check for IG post today
Throws an error if there was no Instagram post by a given user in the last 24 hours.

## Instructions

### Setup

Install packages from `requirements.txt`.

Create the following environment variables:

| Environment variable | Description        | Example    |
|----------------------|--------------------|------------|
| `ig_username`        | Instagram username | `username` |
| `ig_password`        | Instagram password | `password` |
| `USERNAME_TO_CHECK`  | Instagram username of account to check | `username_check` |

#### Sentry

If you have connected [Sentry](https://docs.sentry.io/) to the application, this will receive any exceptions raised.
The environment variable `SENTRY_DSN` should be set to the DSN provided by Sentry.

### Running

When run, the program will throw an exception if the last Instagram post by @`username_check` was not in the last 24 hours.

Instagram may block the login attempt if, for example, you have a new account or you run it from a server hosted in another country to the one that you normally logged in to your account on. The API this runs on recommends you not use your own account.
