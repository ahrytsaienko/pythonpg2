from database import ConnectionFromPool
import requests

class User:
    def __init__(self, email, first_name, last_name, id):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "<User {}>".format(self.email)

    def save_to_db(self):
        with ConnectionFromPool() as connection:
            # cursor create queries and work with results
            with connection.cursor() as cursor:
                # "with" will automatically close cursor after finish
                cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)',
                                (self.email, self.first_name, self.last_name))

    @classmethod
    def load_from_db_by_email(cls, email):
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT * FROM users WHERE email=%s', (email, ))
                user_data = cursor.fetchone()
                return cls(id=user_data[0],
                            email=user_data[1],
                            first_name=user_data[2],
                            last_name=user_data[3]
                            )