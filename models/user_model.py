from config.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    # school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=True)

    # repr method represents how one object of this datatable
    # will look like
    def __repr__(self):
        return f"Name : {self.name}, Email: {self.email}"

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def saveUser(self):
        db.session.add(self)
        db.session.commit()
        return self

    def getUser(self, user_id):
        return User.query.filter_by(id=user_id).first()

    @staticmethod
    def getUserByEmail(email):
        return User.query.filter_by(email=email).first()
