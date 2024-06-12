#!/usr/bin/env python3

class MyString:

  def __init__(self, sentence=""):
    self.sentence=sentence
  
  def get_value(self):
    return self._value

  def set_value(self, value):
    if isinstance(value, str):
      self._value = value
    else: 
      print("The value must be a string.")

  value=property(get_value, set_value)

  def is_sentence(self):
    if self.sentence[-1] == '.':
      return True
    else:
      return False

  def is_question(self):
    if self.sentence[-1] == '?':
      return True
    else:
      return False

  def is_exclamation(self):
    if self.sentence[-1] == '!':
      return True
    else:
      return False
    
  def count_sentences(self):
    count=0
    for i in range(0, len(self.sentence)):
      if self.sentence[i]=='.' and self.sentence[i-1]!='.':
        count+=1
      if self.sentence[i]=='!' and self.sentence[i-1]!='!':
        count+=1
      if self.sentence[i]=='?' and self.sentence[i-1]!='?':
        count+=1
    return count

