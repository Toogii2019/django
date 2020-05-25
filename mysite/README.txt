In order to use API, please authenticate using the username and password and receive a token

Receive a token:
http http://<server>/api-auth-token/ username=$username password=$password

Access to data using a token:

http http://<server>/api-v1/posts/3/ Authorization: Token $token
