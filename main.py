from lib.User import User
from lib.Comments import Comments
from lib.Post import Post


# USER OPERATIONS
print("\n-------------------USER OPERATIONS---------------------------------")
user = User()

# create user
user1_id = user.create_user("Mike", "Mike@GMAIL.COM", 25)
print(f"User {user1_id} created")
user2_id = user.create_user("Kelvin", "kelvim@GMAIL.COM", 30)
print(f"User {user2_id} created")

# fetch user by id
single_user = user.get_user(9)
print("\nFetch user by id ")
print(single_user)

# update user by id
updated_user_id = user.update_user_by_id(5, "John Updated", "johnupdated@gmail.com", 30)
print(f"\nUser {updated_user_id} updated")

# delete user by id
deleted_user_id = user.delete_user_by_id(14)
print(f"\nUser {deleted_user_id} deleted successfully")

# average age of all users
average_age = user.average_age_of_all_users()
print(f"\nAverage age of all users: {average_age[0]}")

# fetch all users
all_users = user.fetch_all_users()
print("\nAll users")
print(all_users)


# POST OPERATIONS
print("\n-------------------POST OPERATIONS---------------------------------")

# create post
print(user1_id)
user_id = user1_id
post = Post()
created_post_id = post.create_post("Post 1", "Post 1 content", user1_id)
print(f"Post {created_post_id} created")

# update post
updated_post = post.update_post_by_id(1, "Post 1 Updated", "Post 1 content updated")
print(f"\nPost {updated_post} updated")

# fetch post by id
single_post = post.get_post_by_id(1)
print("\nFetch post by id ")

# fetch post by user id
posts_by_user_id = post.get_post_by_user_id(4)
print("\nFetch post by user id ")
print(posts_by_user_id)

# fetch all posts
all_posts = post.fetch_all_posts()
print("\nAll posts")
print(all_posts)

# count posts
count_posts = post.count_posts()
print(f"\nTotal number of posts: {count_posts[0]}")




# COMMENTS OPERATIONS
print("\n-------------------COMMENTS OPERATIONS---------------------------------")
create_comment = Comments()
# create comment
comment_id = create_comment.create_comment("This is a comment", 1, 1)
print(f"\nComment {comment_id} created")

# fetch comment by id
single_comment = create_comment.get_comment_by_id(1)
print("\nFetch comment by id ")

# fetch comment by post id
comments_by_post_id = create_comment.get_comment_by_post_id(1)
print("\nFetch comment by post id ")
print(comments_by_post_id)

# fetch all comments
all_comments = create_comment.fetch_all_comments()
print("\nAll comments")
print(all_comments)

# count comments
count_comments = create_comment.count_comments(1)
print(f"\nTotal number of comments: {count_comments[0]}")

#count comments by post id
count_comments_by_post_id = create_comment.count_comments(1)
print(f"\nTotal number of comments for post 1: {count_comments_by_post_id[0]}")

# delete comment by id
deleted_comment_id = create_comment.delete_comment_by_id(1)
print(f"\nComment {deleted_comment_id} deleted successfully")
