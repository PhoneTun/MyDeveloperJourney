from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #Read All
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('user_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users(first_name, last_name, email) values (%(first_name)s, %(last_name)s, %(email)s);"
        results = connectToMySQL('user_schema').query_db(query,data)
        return results
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users where id = %(id)s;"
        results = connectToMySQL('user_schema').query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def update(cls,data):
        query = """UPDATE users 
                set first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW()
                WHERE id = %(id)s;"""
        return connectToMySQL('user_schema').query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM users where id=%(id)s;"
        return connectToMySQL('user_schema').query_db(query,data)