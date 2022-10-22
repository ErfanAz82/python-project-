def triangle(base,height):
    return (base*height)/2

base = int(input("Please enter the base: "))
height = int(input("Please enter the height: "))
print(f"Area of the triangle is {triangle(base,height)}")
