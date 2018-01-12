from user import User

my_user = User.load_from_db_by_email('johndoe@gmail.com')
new_user = User('dan2@gmail.com', 'Dan', 'Does', None).save_to_db()
print(my_user)
user_from_db = User.load_from_db_by_email('dan2@gmail.com')
print(user_from_db)
