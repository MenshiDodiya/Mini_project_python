#Email Validation using if...else

email = input("Enter your Email :- ")
k, j, d = 0,0,0
if len(email) >= 6:#1
    if email[0].isalpha():#2
        if ("@" in email) and (email.count("@") == 1):#3
            if (email[-4] == ".") ^ (email[-3] == "."):#4
                for i in email:
                    if i == i.isspace():#5
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():#5
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:#5
                        d = 1
                if k == 1 or d == 1:
                    print("Wrong email space or special character is not allowed")
                elif j == 1:
                    print("Wrong email no uppercase alphabet allowed")
                else:
                    print("Right Email")
            else:
                print("Wrong email dot(.) is not in right position")
        else:
            print("Wrong email more than 1 @ in email")
    else:
        print("Wrong Email not starting with number")
else:
    print("Wrong Email length is less than 6 character")