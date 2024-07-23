#Conditions for the right email validation using Regex Module
# 1. Starting with alphabet (a-z)
# 2. Not starting with number (0-9)
# 3. The dot(.) and underscore(_) comes 1 time
# 4. The (@) sign comes 1 time
# 5. The dot(.) comes in 2 or 3 position
# 6. Any other special character is not allowed

import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter your email :- ")
if re.search(email_condition,user_email):
    print("Right Email")
else:
    print("Wrong Email")