#-------------VARIABLE--------------------------------------------------------------------------------#
#-----usage---------------------------
# a=10
# A=20
# varshini="apsara"
# _age_=19
# _636="DOB"
# Email_636_id="apsvarsh@gmail.com"

# print(a)
# print(A)
# print(varshini)
# print(_age_)
# print(_636)
# print(Email_636_id)

#-------error-----------------------
# Age=19
# print(age) # error

# if=laptop # error
# print(if)

# 636="numbers" #error
# print(636)
 
#-------------------global variable &  local variable------------------
# x=10 #global
# def assign1():
#     print(x)
# assign1()
# #----------------------
# def assign2():
#     x=20 #local 
#     print(x)
# assign2()
# #----------------------
# a=100 #global
# def show():
#     a=50 #local
#     print(a)
# show()
# print(a)
#------------------------
# a=1
# def assign4():
#     global a
#     a=a+3 
# assign4()
# assign4()
# print(a)
#------------------------
g=100
def assign5():
    x=30
    print("local variable:",x)
    print("global variable:",g)
def assign6():
    global g
    g=g-2
    print(g)
assign5()
assign6()
print(g)



