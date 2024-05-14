#Given an input check if the number is a prime number
def prime_number_checker(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print(f"{num}: is a prime number")
    else:
        print("not a prime number")


prime_number_checker(19)
