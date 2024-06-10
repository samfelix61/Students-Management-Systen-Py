from lib.config import CONN, CURSOR

class Comments:
    # create comment
    @classmethod
    def create_comment(cls, comment, post_id, user_id):
        sql = "INSERT INTO comments(comment, post_id, user_id) VALUES(?, ?, ?)"
        CURSOR.execute(sql, (comment, post_id, user_id))
        CONN.commit()

        return CURSOR.lastrowid

    # get comment by id
    @classmethod
    def get_comment_by_id(cls, comment_id):
        sql = "SELECT * FROM comments WHERE id = ?"
        CURSOR.execute(sql, (comment_id,))
        return CURSOR.fetchone()

    # get comment by post id
    @classmethod
    def get_comment_by_post_id(cls, post_id):
        sql = "SELECT * FROM comments WHERE post_id = ?"
        CURSOR.execute(sql, (post_id,))
        return CURSOR.fetchall()

    # Fetch all comments
    @classmethod
    def fetch_all_comments(cls):
        sql = "SELECT * FROM comments"
        CURSOR.execute(sql)
        return CURSOR.fetchall()

    # delete comment by id
    @classmethod
    def delete_comment_by_id(cls, comment_id):
        sql = "DELETE FROM comments WHERE id = ?"
        CURSOR.execute(sql, (comment_id,))
        CONN.commit()
        return comment_id

    # count comments belonging to a post
    @classmethod
    def count_comments(cls, post_id):
        sql = "SELECT COUNT(*) FROM comments where post_id = ?"
        CURSOR.execute(sql)
        return CURSOR.fetchone()