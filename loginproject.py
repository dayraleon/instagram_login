import request, json


users = [
    {"username": "user1", "password": "password1"},
    {"username": "user1", "password": "password1"}
]

@app.route('/login', methods =['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

#if theres no username or password
    if not username or not password:
        return json({'message': 'Username and password are required.'})
    
# check if the username and passwword match a user in the database
    for user in users:
        if user['username'] == username and user['password'] == password:
            return({'message': 'Login successful'}), 200

    return json({'message':'Invalid username or password.'}), 401

if __name__ == '__main__':
    app.run()


