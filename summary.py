print("--------------------")
print("# Summation Program")
print("# Type 'exit' to end the program")
print("--------------------")

sumData = 0
count = 1
while True:
    data = input(f"Enter number {count}:")

    if(data == "exit"):
        break

    sumData += int(data)
    count = count + 1

print(f"Sum value is {sumData}")