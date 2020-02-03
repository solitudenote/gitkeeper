# gitkeeper

gitkeeper is a tiny microservice that let's a client side appplication authenticate with GitHub.

### Installation

```bash
# Install dependencies
pip3 install -r requirements.txt

# Export env variables
export OAUTH_CLIENT_ID=<client_id>
export OAUTH_CLIENT_SECRET=<client_secret>

# Run the app
flask run
```

### API

```bash
GET http://localhost:5000/authenticate/<code>
```

Sample success response
```json
{
  "access_token": "2e6c49c405c4e059e3ec6d7e57447a6258a53241", 
  "scope": "repo", 
  "token_type": "bearer"
}
```

Sample error response
```json
{
  "error": "bad_verification_code", 
  "error_description": "The code passed is incorrect or expired.", 
  "error_uri": "https://developer.github.com/apps/managing-oauth-apps/troubleshooting-oauth-app-access-token-request-errors/#bad-verification-code"
}
```

### Deploy to Glitch

- Clone repository
```bash
Glitch > New Project > Clone from Git Repo
```
- Set enviornment variables

```bash
OAUTH_CLIENT_SECRET=""
OAUTH_CLIENT_ID=""
```

Or Just clone the [project](https://glitch.com/~solitudenote-gitkeeper).
> Make sure that the Glitch project is private

Feel free to add deployment steps to other platforms.

[Repository](https://github.com/solitudenote/gitkeeper)
