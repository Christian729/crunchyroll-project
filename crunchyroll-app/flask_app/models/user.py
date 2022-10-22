from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0._-]+\.[a-zA-Z]+$')
from flask import flash

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('anime').query_db(query)

        users = []
        
        
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def Save(cls):
        query = "INSERT INTO users (first_name, last_name, email, password,) VALUES ( %(first_name)s , %(last_name)s, %(email)s, %(password)s);"
        results = connectToMySQL('anime').query_db(query)
        print(results)
        return results


    @staticmethod
    def validate_user(user):
        is_valid = True 
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result= connectToMySQL('anime').query_db(query, user)
        
        if len(result) >= 1:
            flash("Email already taken.", "register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", "register")
            is_valid = False
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters", "register")
            is_valid= False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters", "register")
            is_valid= False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters", "register")
            is_valid= False
        if user['password'] != user['confirm']:
            flash("Passwords don't match", "register")
            is_valid= False

        return is_valid