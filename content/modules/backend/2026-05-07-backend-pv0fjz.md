# JWT Sessions vs Opaque Server-Side Sessions
## What
JSON Web Tokens (JWT) and opaque server-side sessions are two approaches to managing user sessions in a backend application. JWT sessions involve storing user data in a JSON Web Token, which is signed and sent to the client, whereas opaque server-side sessions involve storing user data on the server and sending a session ID to the client.

## Why
The choice between JWT sessions and opaque server-side sessions depends on the specific requirements of the application. JWT sessions are useful when the application needs to authenticate users without storing session data on the server, while opaque server-side sessions are useful when the application needs to store sensitive user data on the server.

## How
To implement JWT sessions, the backend generates a JWT token containing user data and sends it to the client. The client then sends the JWT token back to the server with each request, and the server verifies the token before processing the request. To implement opaque server-side sessions, the backend generates a session ID and stores the user data on the server. The client then sends the session ID with each request, and the server retrieves the user data from the server-side storage.

## One exercise or command
To get started with JWT sessions, try running the following command to install the `jsonwebtoken` library: `npm install jsonwebtoken`. Then, generate a JWT token using the `jwt.sign()` function and verify it using the `jwt.verify()` function.

## Further reading
* [Introduction to JSON Web Tokens](https://jwt.io/introduction/)
* [JWT vs Session Cookies](https://stackoverflow.com/questions/71669766/jwt-vs-session-cookies)
* [Using Opaque Tokens with OAuth 2.0](https://oauth.net/2/oauth-token/)
* [Session Management with JWT and Spring Boot](https://www.baeldung.com/spring-security-jwt)
* [Security Considerations for JWT Sessions](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Beginners.html)
