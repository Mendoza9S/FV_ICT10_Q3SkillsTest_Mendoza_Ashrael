from pyscript import document#, display

def character_checker(text):

    has_letter = any(char.isalpha() for char in text)
    has_number = any(char.isdigit() for char in text)

    #conditional statement for determening whether or not the inputed values has a char and number
    if has_letter and has_number:
        return True
    else:
        return False
    
#checks the validation of the inputed username and password by first getting the values of selected values from the index file    
def account_creation(e):
    username = document.getElementById("usernameInput").value
    password = document.getElementById("passwordInput").value
    output = document.getElementById("output")

    if len(username) < 7:
        output.innerText = "Username must be at least 7 characters long"
        return
    if len(password) < 10:
        output.innerText = "Password must be at least 10 characters long"
        return
    if not character_checker(password):
        output.innerText = "Password must contain at least one letter and one number."
        return

    output.innerText = "Account created successfully"

    #display('Account created', target="output")
