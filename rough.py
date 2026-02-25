#polymorphisum--------------
# class cat:
#     def speak(self):
#         print("meow")
# class dog:
#     def speak(self):
#         print("bark")
# obj=cat()
# obj.speak()
# obj=dog()
# obj.speak()

 
#polymorphism with function and arguments--------------
# class tomato:
#     def type(self):
#         print("vegetable")
#     def color(self):
#         print("red")
# class apple:
#     def type(self):
#         print("fruit")
#     def color(self):
#         print("green")
# def fun(obj):
#     obj.type()
#     obj.color()
# obj1=tomato()
# # obj1.type()
# # obj1.color()
# obj2=apple()
# # obj2.type()
# # obj2.color()

# g=10
# def func1():
#     global g
#     print(g)
#     g=g-1
# func1()  
# func1() 
# print(g)



a=10
b="wef" 
try:
    if b==0:
        raise ValueError("division by zero not allow")
    c=a/b
except (ZeroDivisionError,TypeError,NameError) as e:
    print("error:",e)   
else:
    print(c)
finally:
    print("exception completed")
