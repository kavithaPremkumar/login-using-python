import re
import pandas as pd
print("CHOICES")
print("1.Login")
print("2.Register")
print("3.Forgot Password")
print("4.Exit")
choice=int(input("Let us know what you want to do now! "))
if choice == 1:
    login= str(input("Please enter your email :"))
    password=str(input("Please enter your password :"))
    df = pd.read_csv("outfile.csv")
    newdf = df[(df["Email"] == login) & (df["Password"] ==  password)]
    if len(newdf.index) == 0:
        print("You have not registered with us, Request you to select 2 to register")
    else:
        print("Welcome")

elif choice == 2:  # Register
    a= str(input("Please Enter a Valid eMail Id :: "))
    print("Password should contain  one Upper, One lower, one special Char and one number and length should be between 6 and 16 characters")
    p = str(input("Please Enter Your Password :: "))
    a1=a.count("@")
    a2=a.count(".")
    b = a.index("@")
    b1 = a.index(".")
    x=(a[0:b].isalpha())
    if a1==1 and a2==1 and b>0 and len(a[b+1:b1])>0 and x==True and (len(p)>=6 and len(p)<=16) and re.search("[a-z]",p) and re.search("[0-9]",p) and re.search("[A-Z]",p) and re.search("[$#@]",p):
        df1 = pd.DataFrame({"Email": [a]})
        df2 =pd.DataFrame({"Password":[p]})
        df = pd.concat((df1, df2), axis=1)
        df.to_csv("outfile.csv",sep=",",header=False,mode="a")
        print("registation successful")
    else:
        print("Please enter valid email\ password")

elif choice == 3: #Forgot Password
    login= str(input(" Please enter your eMail ID:"))
    df = pd.read_csv("outfile.csv")
    newdf1 = df[(df["Email"] == login)]
    if newdf1.size < 2:
        print("You have not registered with us, Request you to select 1 to register")
    else:
        print(" Your Password from our records is : ", newdf1.at[newdf1.index[0], 'Password'])
else:
    print("Please select available choices")