#import boto3
#from botocore.exceptions import ClientError

def calculate():
    
    while(True):
        num1 = input("Enter first number: ")
        if(num1 == 'q'):
            break
        num2 = input("Enter second number: ")
        if(num2 == 'q'):
            break
        log = num1 + " + " + num2 + " = " + str(int(num1) + int(num2))
        print(log)
        with open('files/calculator-log.txt','a') as file:
            file.writelines(log + "\n")
            
    





def ex4():
    calculate()

ex4()
