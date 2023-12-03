#Write your code below this line 👇

def prime_checker(number):
    if number < 1 :
        print("Not a prime number.")
    else:
        divisors = 0
        list_of_divisors = []
        for num in range(1, (number + 1)):
            if number % num == 0:
                divisors += 1
                list_of_divisors.append(str(num))
        ps = "s" if divisors > 1 else ""
        print(f"{number} has {divisors} divisor{ps} which are: {', '.join(list_of_divisors)}")
        if divisors <= 2:
            print("Is a prime number.")
        else:
            print("Not a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
