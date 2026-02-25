# num1 = int(input("Enter first number (2-digit only): "))


# if num1 < 12 or num1 > 99:
#     print("This trick works only for numbers 12 to 99 only")
# else:
#     sub = num1 - 2
#     predicted = int("2" + str(sub))
#     print("Predicted answer:", predicted)

# # Step 2: Second number
# num2 = int(input("Enter second number: "))

# # Split digits
# a = num2 // 10        # first digit
# b = num2 % 10         # second digit

# host1 = (9 - a) * 10 + (9 - b)
# print("Host number 1:", host1)

# # Step 3: Third number
# num3 = int(input("Enter third number: "))

# # Split digits
# c = num3 // 10
# d = num3 % 10

# host2 = (9 - c) * 10 + (9 - d)
# print("Host number 2:", host2)

# # Step 4: Final sum
# total = num1 + num2 + host1 + num3 + host2

# print("Final total:", total)









n1=int(input("enter first number (2-digit only):"))
if n1<12 or n1>99:
    print("This trick works only for the numbers from 12 to 99 only")

else:
    sub = n1 - 2
    predicted = int("2" + str(sub))
    print("Predicted answer:", predicted)
n2=int(input("enter second number:"))
a=n2//10
b=n2%10
host1=(9-a)*10 + (9-b)
print("host1:",host1)
n3=int(input("ebter third number:"))
c=n3//10
d=n3%10
host2=(9-c)*10 + (9-d)
print("host2:",host2)
total=n1+n2+host1+n3+host2
print("finally result:",total)















