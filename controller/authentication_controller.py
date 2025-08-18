from models.user_model import User


class AuthenticationController():
    def register_user(self, data):
        if not data:
            return "<p>No data provided for registration!</p>", 400
        if "name" not in data or "password" not in data:
            return "<p>Name and password are required!</p>", 400
        name = data.get('name')
        password = data.get('password')
        email = data.get('email')
        user = User(name=name, email=email, password=password)

        try:
            user.saveUser()
        except Exception as e:
            return f"<p>Error saving user: {e}</p>", 500

        return f"Registering user: {name} with password: {password}", 201

    def getUser(self, email):
        user = User.getUserByEmail(email)
        if user:
            return f"User found: {user.name}, {user.email}", 200
        return "<p>User not found!</p>", 404

    def login_user(self):
        return "<p>User logged in successfully!</p>"

    def logout_user(self):
        return "<p>User logged out successfully!</p>"
