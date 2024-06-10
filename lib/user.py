from lib.config import CONN, CURSOR

class User:
    # add user
    @classmethod
    def create_user(cls, name, email, age):
        sql = "INSERT INTO users(name, email, age) VALUES(?, ?, ?)"
        CURSOR.execute(sql, (name, email, age))
        CONN.commit()
        return CURSOR.lastrowid

    # Get user by id
    @classmethod
    def get_user(cls, user_id):
        sql = "SELECT * FROM users WHERE id = ?"
        CURSOR.execute(sql, (user_id,))
        return CURSOR.fetchone()

    # Update user by id
    @classmethod
    def update_user_by_id(cls, user_id, name, email, age):
        sql = "UPDATE users SET name = ?, email = ?, age = ? WHERE id = ?"
        CURSOR.execute(sql, (name, email, age, user_id))
        CONN.commit()
        return user_id

    # delete user by id
    @classmethod
    def delete_user_by_id(cls, user_id):
        sql = "DELETE FROM users WHERE id = ?"
        CURSOR.execute(sql, (user_id,))
        CONN.commit()
        return user_id

    # Average age of all users
    @classmethod
    def average_age_of_all_users(cls):
        sql = "SELECT AVG(age) FROM users"
        CURSOR.execute(sql)
        return CURSOR.fetchone()

    # Fetch all users
    @classmethod
    def fetch_all_users(cls):
        sql = "SELECT * FROM users"
        CURSOR.execute(sql)
        return CURSOR.fetchall()