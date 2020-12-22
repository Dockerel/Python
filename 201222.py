class myclass:
    def __init__(self, *args):
        self.var='hello'
        print('myclass : instant var is created')

obj=myclass()
print(obj.var)