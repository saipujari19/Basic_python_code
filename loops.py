#current = 1
#number = 100
#sum = 0
#while current <= number:
    #sum = sum + current
    #print(sum)
for x in range(1, 10):
    print(x * 0.1, 1)
number = input(int("enter the number:"))
current = number
while current >=0:
    print(current)
    current = current - 5

start = 11
end = 21


def is_prime(start):
    pass


while start <= end:
    if is_prime(start):
        print(start)

        break
    start = start +1
start = 34
end = 65
for number in range(start, end+1):
    if number % 2 == 0:
        pass
    else:
        print(number)

start = 34
end = 65
for number in range(start, end + 1):
    if number % 2 == 0:
        continue
    print(number)



