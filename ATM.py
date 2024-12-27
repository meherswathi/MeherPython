#Write a Python code to know how many 500 , 200, 100 Notes are dispensed through ATM

amt=int(input("Enter the Total Amount:"))
FiveHundread=amt//500
FiveRem=amt%500
TwoHundread=FiveRem//200
TwoRem=FiveRem%200
OneHundread=TwoRem//100
OneRem=TwoRem%100
print("*"*100)
print("\t\t How Many 500,200,100 Rupee Notes are Dispensed from ATM")
print("*"*100)
print("\t\t Number of 500 Rupee Notes={}".format(FiveHundread))
print("*"*100)
print("\t\t Number of 200 Rupee Notes={}".format(TwoHundread))
print("*"*100)
print("\t\t Number of 100 Rupee Notes={}".format(OneHundread))
print("*"*100)




