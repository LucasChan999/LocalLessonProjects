#Operate:Combine the name and function class
#Lucas
#2017/5/24
class Operate:
    Max = 1000
    #FunctionName = {"sin", "cos",  "tg","ctg","log","lg","ln","PI", "E"}
    def isNumber( c):
        if (c >= '0' and c <= '9'):
               return True
        return False

    def isChar(c):
        if ((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == '_'):
		    return True
	    return False
    
    def isOperaters(c):
        for case in c:
          if case('?'):
             return 10 
             break
	      if case(';'):return 11
	      if case('('):return 12
	      if case(')'):return 13
	      if case( '+'):return 14
	      if case('-'):return 15
	      if case('*'):return 16
	      if case('/'):return 17
	      if case('='):return 18
	      if case('^'):return 19
            
 #   Word[]
 #   num[]
 #   startPostion = 0		#字符开始位置
	#nowPostion = 0	#字符当前位置
 #   length 	= 0	
	#def __init__(self,s):
 #     self.s = s
	#  self.startPostion = 0
	#  self.nowPostion = 0
	#  self.length = 0

	#def getWordAndNum():

	#def isNumber( c):

	#def isChar( c):

 #   #bool isChar(char c);
	#def isOperaters(char c):

	#def isblank(char c):

	#def addWords(string s, int n):

    
    
    




