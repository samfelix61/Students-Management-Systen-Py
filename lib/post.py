from lib.config import CONN, CURSOR

class Post:
    # create post
    @classmethod
    def create_post(cls, title, content, user_id):
        sql = "INSERT INTO posts(title, content, user_id) VALUES(?, ?, ?)"
        CURSOR.execute(sql, (title, content, user_id))
        CONN.commit()

        return CURSOR.lastrowid

    # get post by id
    @classmethod
    def get_post_by_id(cls, post_id):
        sql = "SELECT * FROM posts WHERE id = ?"
        CURSOR.execute(sql, (post_id,))
        return CURSOR.fetchone()

    # get post by user id
    @classmethod
    def get_post_by_user_id(cls, user_id):
        sql = "SELECT * FROM posts WHERE user_id = ?"
        CURSOR.execute(sql, (user_id,))
        return CURSOR.fetchall()

    # Fetch all posts
    @classmethod
    def fetch_all_posts(cls):
        sql = "SELECT * FROM posts"
        CURSOR.execute(sql)
        return CURSOR.fetchall()

    # delete post by id
    @classmethod
    def update_post_by_id(cls, post_id, title, content):
        sql = "UPDATE posts SET title = ?, content = ? WHERE id = ?"
        CURSOR.execute(sql, (title, content, post_id))
        CONN.commit()
        return post_id

    # count posts
    @classmethod
    def count_posts(cls):
        sql = "SELECT COUNT(*) FROM posts"
        CURSOR.execute(sql)
        return CURSOR.fetchone()

    
