#Lexical analyzer
#lucas
#2017/6/13
#Python 2.7
import string as st
class Operate(object):
  """Operate Class"""
  def __init__(self,word = [1000],num = [1000],):
        self.str =  [] #need to write another input function
        self.nowposition = 0
        self.length = 0
        self.Max = 1000     
        self.FunctionName = ["sin", "cos",  "tg","ctg","log","lg","ln","PI", "E"]
        self.word = word
        self.num = num

  def  _getWordAndNum(self):
       for iter in range(self.length):
         print "<",word[iter],',',num[iter],'>'
  
  def _isNumber(self,c):
      if c>= '0' and c<= '9':
          return True
      return False
   
  def _isChar(self,c):
     if ((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == '_'):
          return True
     return False
 
  def _isOperaters(self,c):
     import swtich as s
     switch = s.swtich
     for case in switch(c):
        if case('?'):
            return 10
        if case(';'):
            return 11
        if case('('):
            return 12
        if case (')'):
            return 13
        if case("+"):
            return 14
        if case('-'):
            return 15
        if case('*'):
            return 16
        if case('/'):
            return 17
        if case('='):
            return 18
        if case('^'):
            return 19
        if case():
            return 0

  def _isblank(self,c):
      import swtich as s
      switch = s.swtich
      for case in switch(c):
       if case(' '):
          return True
       if case('\t'):
          return True
       if case('\n'):
          return True
       if case():
          return False
   
  def _addWords(self,s = [],n = int):
      self.word[self.length] = s
      self.num[self.length] = n
      self.length += 1
  
  def _isKey(self,s= []):
      for iter in range(9):
          if s == self.FunctionName[iter]:
              return iter + 1
      return 0

  def _work(self,s = []):
       self.longs = len(s)
         