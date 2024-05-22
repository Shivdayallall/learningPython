# When creating a class that uses an init method, must  pass self as paramater along with any default paramter you want when the class is instantiated.
# This means that when the class is first instantiated it must have default argunments.
# If you want to provide default value for the class when it get instantiated you can define it within the method.
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.followers = 0
        self.following = 0
        print("user is being created")

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("01", "Shiv")
user2 = User("002", "Lall")
user1.follow(user2)

print(user1.following)
print(user1.followers)

print(user2.following)
print(user2.followers)