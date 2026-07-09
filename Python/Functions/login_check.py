def check_login(username,password):

    print("Login Successfull" if username == "admin" and password == 1234 else "Incorrect username or paasword")

check_login("admin",1234)