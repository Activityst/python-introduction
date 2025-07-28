def fizzbuzz(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0 :
        return "FizzBuzz"
    elif number % 3 == 0 or '3' in str(number):
        return "Fizz"
    elif number % 5 == 0 or '5' in str(number):
        return "Buzz"
    else:
        return str(number)

def compute():
    for i in range(1, 101):
        print(f"{i} => {fizzbuzz(i)}")
compute()