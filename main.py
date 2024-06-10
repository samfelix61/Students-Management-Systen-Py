from lib.user import User
from lib.comments import Comments
from lib.post import Post
import sys

def main_menu():
    while True:
        print("=============MAIN MENU=================")
        print("1.Manage users")
        print("2.Manage posts")
        print("3.Manage comments")
        print("4.Exit")

        choice = input("\nEnter your choice: ")
        if choice =="1":
            return user_operations()

        elif choice =="2":
            return post_operations()
        
        elif choice =="3":
            return comments_operations()

        elif choice =="4":
            sys.exit()
        
        else:
            print("Invalid Input")
        


def user_operations():
    while True:
        print("\n*******USER MENU********")
        print("1.Add user")
        print("2.Update user")
        print("3.Fetch all users")
        print("4.Fetch user by id")
        print("5.Get average age of all users")
        print("6.Delete user")
        print("7.Retun to main menu")

        choice = input("\nEnter your choice: ")
        
        user = User()
        if choice =="1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            age = input("Enter age: ")

            user_id = user.create_user(name, email, age)
            print(f"User with id {user_id} added successfully")
          

        elif choice =="2":
            user_id = input("Enter the id of the user you want to update: ")
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            age = input("Enter new age: ")

            userID = user.update_user_by_id(user_id , name, email, age)
            print(f"User with id {userID} updated successfully")
            

        elif choice =="3":
            all_users = user.fetch_all_users()
            print("\nAll users")
            print(all_users)

        elif choice =="4":
            user_id = input("Enter the id of the user you want to fetch: ")
            single_user = user.get_user(user_id)
            print(single_user)


        elif choice =="5":
            average_age = user.average_age_of_all_users()
            print(f"\nAverage age of all users: {average_age[0]}")


        elif choice =="6":
            user_id = input("Enter the id of the user you want to delete: ")
            deleted_user_id = user.delete_user_by_id(user_id)
            print(f"\nUser {deleted_user_id} deleted successfully")


        elif choice =="7":
            return main_menu()
        
        else:
            print("Invalid Input")

    

def post_operations():
    while True:
        print("\n*******POST MENU********")
        print("1.Add post")
        print("2.Update post")
        print("3.Fetch all posts")
        print("4.Fetch post by id")
        print("5.Fetch posts by user id")
        print("6.Count all posts")
        print("7.Retun to main menu")


        choice = input("\nEnter your choice: ")

        post = Post()
        if choice=="1":
            title = input("Enter title: ")
            content = input("Enter content: ")
            user_id = input("Enter user id: ")

            
            created_post_id = post.create_post(title, content, user_id)
            print(f"Post {created_post_id} created")

        elif choice=="2":
            post_id = input("Enter post id: ")
            title = input("Enter new title: ")
            content = input("Enter new content: ")

            updated_post = post.update_post_by_id(post_id, title, content)
            print(f"\nPost {updated_post} updated")

        elif choice=="3":
            all_posts = post.fetch_all_posts()
            print("\nAll posts")
            print(all_posts)
        
        elif choice=="4":
            post_id = input("Enter post id: ")
            single_post = post.get_post_by_id(post_id)
            print("\nFetch post by id ")
            print(single_post)
        
        elif choice=="5":
            user_id = input("Enter user id: ")

            posts_by_user_id = post.get_post_by_user_id(user_id)
            print("\nFetch post by user id ")
            print(posts_by_user_id)

        elif choice=="6":
            count_posts = post.count_posts()
            print(f"\nTotal number of posts: {count_posts[0]}")
        
        elif choice=="7":
            return main_menu()

        else:
            print("Invalid Input")



def comments_operations():
    while True:
        print("\n*******COMMENTS MENU********")
        print("1.Add comment")
        print("2.Update comment")
        print("3.Fetch all comment")
        print("4.Fetch comments by user id")
        print("5.Fetch comments by post id")
        print("6.Count all comments")
        print("7.Delete comment")
        print("8.Retun to main menu")


        choice = input("\nEnter your choice: ")

        comment = Comments()

        if choice=="1":
            user_id = input("Enter user id: ")
            post_id = input("Enter post id: ")
            comment_ = input("Enter comment: ")
            comment_id = comment.create_comment(comment_, post_id, user_id)

            print(f"\nComment {comment_id} created")

        elif choice=="2":
            pass
        
        elif choice=="3":
            all_comments = comment.fetch_all_comments()
            print("\nAll comments")
            print(all_comments)

        elif choice=="4":
            user_id = input("Enter user id: ")
            comments_by_user_id = comment.get_comment_by_user_id(user_id)
            print("\nFetch comment by user id ")
            print(comments_by_user_id)

        elif choice=="5":
            post_id = input("Enter post id: ")
            comments_by_post_id = comment.get_comment_by_post_id(post_id)
            print("\nFetch comment by post id ")
            print(comments_by_post_id)

        elif choice=="6":
            count_comments = comment.count_comments()
            print(f"\nTotal number of comments: {count_comments[0]}")
        
        elif choice=="7":
            comment_id = input("Enter comment id: ")
            deleted_comment_id = comment.delete_comment_by_id(comment_id)
            print(f"\nComment {deleted_comment_id} deleted successfully")   

        elif choice=="8":
            return main_menu()


main_menu()







