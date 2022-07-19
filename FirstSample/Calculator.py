
print(" 1 Addition")
print(" 2 subtraction")
print(" 3 multiplication")
print(" 4 Division")

choice= input ("Enter your choice")

5
num1=float(input("Enter Number 1 :"))
num2=float(input("Enter Number 2 :"))

if choice =="1":
    print(num1,"+", num2,"=",(num1+num2))
elif choice == "2":
    print(num1,"-", num2,"=",(num1-num2))
elif choice == "3":
    print(num1,"*", num2,"=",(num1*num2))
elif choice =="4" :
    if num2== 0.0 :
        print("Divide by 0 Error")
    else:
        print (num1,"/" , num2, "=",(num/num2))
      

