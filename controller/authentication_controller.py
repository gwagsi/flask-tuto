class AuthenticationController():
    def register_user(self, data):
        if not data:
            return "<p>No data provided for registration!</p>", 400
        if "username" not in data or "password" not in data:
            return "<p>Username and password are required!</p>", 400
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        print(f"Registering user: {username} with password: {password}")
        return f"Registering user: {username} with password: {password}"

    def login_user(self):
        return "<p>User logged in successfully!</p>"

    def logout_user(self):
        return "<p>User logged out successfully!</p>"
