# def func_name(variable_name: type) -> return_type:

age: int
name: str
height: float
is_human: bool

def police_check(age: int) -> bool:
    if age > 15:
        can_drive = True
    else:
        can_drive = False
    return can_drive

person_age = int(input("What is your current age?\n> "))

if police_check(person_age):
    print("You may pass.")
else:
    print("Pay fine.")
