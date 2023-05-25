

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            #raise ValueError("Radius must be a positive value.")
            print("Radius must be a positive value.")
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, new_radius):
        if new_radius <= 0:
            #raise ValueError("Radius must be a positive value.")
            print("Radius must be a positive value.")
        self._radius = new_radius
    
    def area(self):
        return 3.14159 * self._radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self._radius
    
    def __repr__(self):
        return f"Circle(radius={self._radius})"
    
    def __mul__(self, other):
        if isinstance(other, int) and other > 0:
            return Circle(self._radius * other)
        else:
            #raise ValueError("Circle can only be multiplied by a positive integer.")
            print("Circle can only be multiplied by a positive integer.")


# Create a circle with radius 5
circle1 = Circle(5)
print(circle1.area())  # Output: 78.53975
print(circle1.perimeter())  # Output: 31.4159
print(circle1.radius)  # Output: 5

# Modify the radius of the circle
circle1.radius = 8
print(circle1.radius)  # Output: 8

# Try to set an invalid radius (<= 0)
circle1.radius = -2  # Raises a ValueError with the error message

# Create a new circle using multiplication
circle2 = circle1 * 3
print(circle2.radius)  # Output: 24

# Try to multiply with an invalid number (<= 0)
circle3 = circle1 * -2  # Raises a ValueError with the error message

# Print the circle objects
print(circle1)  # Output: Circle(radius=8)
print(circle2)  # Output: Circle(radius=24)
