#!/usr/bin/env python

from user import User
from teacher import Teacher

class Student(User):
    def __init__(self, first_name = "My",last_name="Student"):
        super().__init__(first_name=first_name, last_name=last_name)
        self.knowledge=[]

    def learn(self,info):
        self.knowledge.append(info)
