def hello(name):
    print(f"Hello {name}")


def area(width, height):
    total = width*height
    return total


hello("Zen")

print(area(5, 6))
print(area(5.5, 9))


def show_info(name="", salary=0.00, lang="not define"):
    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Language: {lang}")


show_info()
show_info("Zen", 155584)
