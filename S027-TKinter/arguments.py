def add(*args):
    sum = 0
    print(args)
    print(type(args))
    for n in args:
        sum += n
    return sum


print(f"1 + 2 + 3 + 4 + 5 + 6 = {add(1, 2, 3, 4, 5, 6)}")


def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")

my_car = Car(make="Nissan", model="GTR")
print(my_car.model)
print(my_car.colour)
