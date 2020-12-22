# -*- coding: utf-8 -*-

class myclass:
    def __init__(self, *args): #인스턴트 객체 자동생성
        self.var='hello'
        print('myclass : instant var is created')

obj=myclass()
print(obj.var)