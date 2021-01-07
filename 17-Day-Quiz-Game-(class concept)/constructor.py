class User:
    
    
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0
        
    def follow(self,user):
        user.following += 1
        self.followers += 1
    
    
user_1 = User("001", "Nandy")
user_2 = User("002","Akash")
user_2.follow(user_1)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
