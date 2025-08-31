class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow_user(self, user):
        user.followers += 1
        self.following += 1

user1 = User('001','Alice')
user2 = User('002','Bob')

print(user1)
print(user2)
print('----------------------------------------------')
print(user1.id, user1.username, user1.followers)
print(user2.id, user2.username, user2.followers)

user1.follow_user(user2)
print('----------------------------------------------')
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)