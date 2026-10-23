correct_pin = "1234"
tries = 0 
access = False 

while tries < 3 and not access:
    pin = input("PIN: ")
    tries += 1

if pin == correct_pin:
    print("Access granted")
    access = True

if not access:
    print("Card blocked")