import math
from Package.Shape import Shape, Line


class Triangle(Shape):
    def __init__(self, vertices=None, edges=None, inner_angles=None, is_regular=False):
        super().__init__(vertices, edges, inner_angles, is_regular)
                       
        if not self.edges and self.vertices:      
            self.define_edges()
        elif not self.vertices and self.edges:
            self.define_vertices() 
        
        if len(self.vertices) != 3 or len(self.edges) != 3:
            raise ValueError("A triangle has exaclty 3 edges or 3 vertices")
       
        
    def define_edges(self):
        self.edges = [
            Line(self.vertices[0], self.vertices[1]),
            Line(self.vertices[1], self.vertices[2]),
            Line(self.vertices[2], self.vertices[0])
        ]

    def define_vertices(self):
        self.vertices = [
            self.edges[0].start,
            self.edges[0].end,
            self.edges[1].end,
        ]
    
    def compute_perimeter(self):
        perimeter = 0
        for edges in self.edges:
            perimeter += edges.lenght()
        return perimeter
    
    def compute_area(self):
        a = self.edges[0].lenght()
        b = self.edges[1].lenght()
        c = self.edges[2].lenght()
        
        s = (a + b + c) / 2
        
        return (s * (s - a) * (s-b) * (s-c)) ** 0.5
    
    
class Equilateral(Triangle):
    def __init__(self, vertices=None, edges=None, inner_angles=None, is_regular=False):
        super().__init__(vertices, edges, inner_angles, is_regular)
        self.inner_angles = [60,60,60]


class Isosceles(Triangle):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices, edges)
        
        self.compute_inner_angles()
    
    def compute_inner_angles(self):

        a = self.edges[0].lenght()
        b = self.edges[1].lenght()
        c = self.edges[2].lenght()

        if a == b:
            equal_side = a
            base = c
        elif a == c:
            equal_side = a
            base = b
        else:
            equal_side = b
            base = a

        angle_base = math.degrees(math.acos((2 * equal_side**2 - base**2) / (2 * equal_side**2)))
        angle_equal = (180 - angle_base) / 2
        
        self.inner_angles = [angle_equal, angle_equal, angle_base]
        

class Scalene(Triangle):
    def __init__(self, vertices=None, edges=None, inner_angles=None, is_regular=False):
        super().__init__(vertices, edges, inner_angles, is_regular)  
        self.compute_inner_angles()
        
    def compute_inner_angles(self):        
        a = self.edges[0].lenght()
        b = self.edges[1].lenght()
        c = self.edges[2].lenght()
        

        angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        angle_C = 180 - angle_A - angle_B
        
        self.inner_angles = [angle_A, angle_B, angle_C]


class TriRectangle(Triangle):
    def __init__(self, vertices=None, edges=None, inner_angles=None, is_regular=False):
        super().__init__(vertices, edges, inner_angles, is_regular)
        
        self.compute_inner_angles()
    
    def compute_inner_angles(self):
        a = self.edges[0].lenght()
        b = self.edges[1].lenght()
        c = self.edges[2].lenght()
        
        sides = sorted([a, b, c]) 
        leg1, leg2, hypotenuse = sides
        

        angle1 = math.degrees(math.asin(leg1 / hypotenuse))
        angle2 = 90 - angle1 
        
        self.inner_angles = [angle1, angle2, 90]