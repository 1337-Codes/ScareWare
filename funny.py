import os
name = os.getenv("COMPUTERNAME")
given_name = input("Your name is: ")
if given_name.upper() == name.upper():
    print("I did not expect the truth...")
else:
    print(f"Nah, bruv. That's cap. I know who you are, {name}.")