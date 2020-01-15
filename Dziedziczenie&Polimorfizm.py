# Dziedziczenie

class Rectangle (object):
        def __init__(self,w,h):
            self.w = w
            self.h = h
            def area(self):
                return self.w * self.h
            
class Square (Rectangle):
     def __init__(self,a):

         super().__init__(a,a)
   
r = Rectangle(3,7)       
s = Square(4)  
print(s.area())    
           

# Polimorfizm
class Rectangle (object):
        def __init__(self,w,h):
            self.w = w
            self.h = h
            def area(self):
                return self.w * self.h
            def angle(self):
                
 class Square (Rectangle):
     def __init__(self,a):

         super()__init(a,a)__
     def angle(self):
         return 90
       
s = Square(4)  
print(s.angle())   
