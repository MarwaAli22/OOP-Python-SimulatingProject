def email_validation(email:str):
    #check email not null
    if not email :
        raise TypeError("Email cannot be empty.")
    #check email start with string
    if not email[0].isalpha() :
        raise SyntaxError("Email must start with an alphabetic character.")
    #check email is strep
    for i in email:
        if i == " ":
            raise SyntaxError("Email cannot contain spaces.")
    #check (example@email.com)
    if "@" and "."in email:
        username, domain = email.split("@")
        if username and domain :
            x , y = domain.split(".")
            if x and y:
                return True
    raise ValueError("Invalid email format.")
