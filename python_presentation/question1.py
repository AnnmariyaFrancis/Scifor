# -*- coding: utf-8 -*-
"""question1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P_isDujU26Uu3zrzDv92QK93D6aSKPxH
"""

#len
class Person:
  def __init__(self,val):
    self.val=val
    self.space=" "
  def __add__(self,val2):
    return Person(self.val+self.space+val2.val)
ob=Person("Ann")
ob2=Person("Mariya")
ob3=ob+ob2
print(ob3.val)