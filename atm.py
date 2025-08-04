correct_pin=input("Set your 4-digit ATM pin:")
balance=10000
attempts=0
while attempts<3:
   user_pin=input("Enter your pin no:")

   if user_pin==correct_pin:
       print("Access granted--")

       while True:

         show='''
       please select any one option:
       1. check balance
       2. deposit balance
       3. withdraw balance
       4. Exit
    
       '''
         print(show)
         option=int(input("Enter any option:"))
         if option==1:
            print("Current balance is :",balance)
         elif option==2:
            amount=int(input("Enter amonut to deposit:"))
            if amount>0:
                balance+=amount
                print("Deposit successfull. New balance is :",balance)
            else:
                print("Invalid deposit amount")
         elif option==3:

            withdraw=int(input("enter amount which you want to withdraw:"))
            if withdraw<=balance and withdraw>0:
               balance-=withdraw
               print(" withdraw successfull. YOur remaining amount is :",balance)
            elif withdraw<=0:
                print("Enter a valid amount to wihdraw")
            else:

               print("Insufficient balance.Your balance is ",balance)
         elif option==4:
               print("Thank you for using ATM.Good bye!")
               exit()
         else:
               print("Please enter valid option")
   else:
       attempts+=1
       print("Incorrect PIN .try again!")
if attempts==3:
    print("Too many incorrect attempts .Card Blocked---")





