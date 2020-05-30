In order to use API, please authenticate using the username and password and receive a token

Receive a token:
http http://gentle-cove-01948.herokuapp.com/api-auth-token/ username=django password=djangouw123

Access to data using a token:

http https://gentle-cove-01948.herokuapp.com/api-v1/posts/3/ "Authorization: Token $token"
