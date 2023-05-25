
import unittest

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive value.")
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, new_radius):
        if new_radius <= 0:
            raise ValueError("Radius must be a positive value.")
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
            raise ValueError("Circle can only be multiplied by a positive integer.")


class TestCircle(unittest.TestCase):
    def test_initialization(self):
        # Test initialization with valid radius
        circle = Circle(5)
        self.assertEqual(circle.radius, 5)
        
        # Test initialization with invalid radius
        with self.assertRaises(ValueError):
            circle = Circle(-2)
    
    def test_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53975, places=4)
        
        circle.radius = 8
        self.assertAlmostEqual(circle.area(), 201.06176, places=4)
    
    def test_perimeter(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.perimeter(), 31.4159, places=4)
        
        circle.radius = 8
        self.assertAlmostEqual(circle.perimeter(), 50.26544, places=4)
    
    def test_multiplication(self):
        circle = Circle(5)
        
        # Test multiplication with valid integer
        circle2 = circle * 3
        self.assertEqual(circle2.radius, 15)
        
        # Test multiplication with invalid integer
        with self.assertRaises(ValueError):
            circle3 = circle * -2
    
    def test_representation(self):
        circle = Circle(5)
        self.assertEqual(repr(circle), "Circle(radius=5)")
        
        circle.radius = 8
        self.assertEqual(repr(circle), "Circle(radius=8)")

if __name__ == '__main__':
    unittest.main()
