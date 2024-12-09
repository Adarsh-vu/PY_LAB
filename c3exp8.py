def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
def pr(n):
        count=0
        for i in range (1,n+1):
                if n%i==0:
                        count=count+1
        if count>2:
                return 0
        else:
                return 1
def sum_digits_in_range(upper_limit):
    for num in range(1, upper_limit + 1):
        digit_sum = sum_of_digits(num)
        if pr(digit_sum):
            print(f"Sum of digits of {num} is {digit_sum}, which is prime.")

limit = int(input("Enter an upper limit: "))
sum_digits_in_range(limit)
