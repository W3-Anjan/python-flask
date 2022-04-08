#### create virtual environment
``python3 -m venv ./env``
#### activate env
``source env/bin/activate``



#### Stateful protocol vs stateless protocol
https://www.youtube.com/watch?v=_3NKBHYcpyg

Traditional approach: 
1. After login to a website with user name and password, the server stores 
a session in the database, and response to client with a session id.
2. Inside the browser the session id is stored in a Cookie. Cookie is a text file 
inside the browser local storage in the form of a key value pair.
3. This Cookie will be sent back to server for every subsequent request.
4. Server will response to that request if user is currently loggedin.
5. This is called stateful protocol. So, stateful protocol saves everything in the backend.



Json Web Token (JWT) based approach:
1. After login, the server generates a private key JWT, rather than storing the session in database.
2. The JWT is then received by the client and stores in local storage.
3. The JWT will be sent in the Auth header and the server validates the token by a signature.
4. Here nothing is stored inside server. This is called stateless protocol.
5. The stateless protocol saves everything in th frontend/client side.

#### Generating signature key in terminal to verify the JWT token
1. There are different ways to generate signature key. This signature key remains inside server to create a JWT after user login.
2. inside terminal: python3
    1. import os
    2. os.urandom(12)

    1. import uuid
    2. uuid.uuid4().hex 'aed28d4f894f476b9435456281f8e399'

    1. import secrets (applicable for python > 3.7)
    2. secrets.token_urlsafe(12) '5aVESAbddgHg1Dva'

#### Creating JWT with the combination of Secret key
https://jwt.io/
create a JWT token with the combination of username + expiry time + SERVER_SIGNATURE_KEY

        ```token = jwt.encode({
            'user':request.form['username'],
            'expiration': str(datetime.utcnow() + timedelta(seconds=120)) # expired in 2 min
        },app.config['SECRET_KEY'])  ```   

#### Semantic UI for design    


