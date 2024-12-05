
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14159
    def area(self):
        return self.pi * self.radius ** 2
    def circumference(self):
        return 2 * self.pi * self.radius

radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
print(f"Area: {circle.area():.2f}")
print(f"Circumference: {circle.circumference():.2f}")
