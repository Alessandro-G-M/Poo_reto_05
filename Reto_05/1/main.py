from Package.Rectangle import *
from Package.Triangle import *
from Package.Shape import *

def main():
    
    rectangle = Rectangle(vertices=[Point(0, 0), Point(4, 0), Point(4, 3), Point(0, 3)])
    square = Square(vertices=[Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)])
    equilateral_triangle = Equilateral(vertices=[Point(0, 0), Point(2, 0), Point(1, math.sqrt(3))])
    isosceles_triangle = Isosceles(vertices=[Point(0, 0), Point(2, 0), Point(1, 2)])
    scalene_triangle = Scalene(vertices=[Point(0, 0), Point(3, 0), Point(2, 2)])
    tri_rectangle = TriRectangle(vertices=[Point(0, 0), Point(3, 0), Point(3, 4)])


    print("Rectangle Perimeter:", rectangle.compute_perimeter())
    print("Rectangle Area:", rectangle.compute_area())

    print("Square Perimeter:", square.compute_perimeter())
    print("Square Area:", square.compute_area())


    print("Equilateral Triangle Perimeter:", equilateral_triangle.compute_perimeter())
    print("Equilateral Triangle Area:", equilateral_triangle.compute_area())


    print("Isosceles Triangle Perimeter:", isosceles_triangle.compute_perimeter())
    print("Isosceles Triangle Inner Angles:", isosceles_triangle.inner_angles)
    print("Isosceles Triangle Area:", isosceles_triangle.compute_area())


    print("Scalene Triangle Perimeter:", scalene_triangle.compute_perimeter())
    print("Scalene Triangle Inner Angles:", scalene_triangle.inner_angles)
    print("Scalene Triangle Area:", scalene_triangle.compute_area())


    print("Right Triangle Perimeter:", tri_rectangle.compute_perimeter())
    print("Right Triangle Inner Angles:", tri_rectangle.inner_angles)
    print("Right Triangle Area:", tri_rectangle.compute_area())
    
    
if __name__ == '__main__':
    main()
