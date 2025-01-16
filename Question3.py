class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def calculate_area(self):
        return self.width * self.height

# Create instances of Rectangle and Square
rectangle = Rectangle(5, 7)
square = Square(4)

# Print the areas
print("Rectangle Area:", rectangle.calculate_area())
print("Square Area:", square.calculate_area())