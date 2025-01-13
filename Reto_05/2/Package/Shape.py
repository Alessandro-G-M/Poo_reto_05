import math

class Point:
  def __init__(self, x:float = 0, y:float = 0):
    self.x = x
    self.y = y

  def move(self, new_x:float, new_y:float):
    self.x = new_x
    self.y = new_y

  def reset(self):
    self.x = 0
    self.y = 0

  def compute_distance(self, point:"Point") -> float:
    distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
    return distance


class Line:
    def __init__(self, start:Point, end:Point):
        self.start = start
        self.end = end
        
    def lenght(self):
        return ((self.end.x - self.start.x)**2 + (self.end.y - self.start.y)**2)**0.5
        
        
class Shape:
    def __init__(self, vertices = None, edges = None, inner_angles = None, is_regular = False):
        self.vertices = vertices if vertices is not None else []
        self.edges = edges if edges is not None else []
        self.inner_angles = inner_angles if inner_angles is not None else [] 
               
        if not self.edges and self.vertices:      
            self.define_edges()
        elif not self.vertices and self.edges:
            self.define_vertices()
            
    def define_edges(self):
        pass
    
    def define_vertices(self):
        pass
            
    def compute_perimeter(self) -> float:
        pass
    
    def compute_area(self) -> float:
        pass
    
    def es_regular(self):
        same_edges = all(lado == self.edges[0] for lado in self.edges)
        same_inner_angles = all(angulo == self.inner_angles[0] for angulo in self.inner_angles)
        return same_edges and same_inner_angles


class Rectangle(Shape):
    def __init__(self, vertices=None, edges=None, inner_angles = [90,90,90,90]):
       super().__init__(vertices, edges, inner_angles)
       self.inner_angles = inner_angles
       
       if not self.edges and self.vertices:
           self.define_edges()
       elif not self.vertices and self.edges:
           self.define_vertices()
           
       if len(self.vertices) != 4 or len(self.edges) != 4:
            raise ValueError("A rectangle has exaclty 4 edges or 4 vertices")

    def define_edges(self):
        self.edges = [
            Line(self.vertices[0], self.vertices[1]),
            Line(self.vertices[1], self.vertices[2]),
            Line(self.vertices[2], self.vertices[3]),
            Line(self.vertices[3], self.vertices[0])
        ]

    def define_vertices(self):
        self.vertices = [
            self.edges[0].start,
            self.edges[0].end,
            self.edges[1].end,
            self.edges[2].end
        ]
    
    def compute_perimeter(self) -> float:
        perimeter = 0
        for edges in self.edges:
            perimeter += edges.lenght()
            
        return perimeter
    
    def compute_area(self) -> float:
        base = self.edges[0].lenght()
        height = self.edges[1].lenght()
        
        return base * height
        

class Square(Rectangle):
    def __init__(self, vertices=None, edges=None, inner_angles=[90, 90, 90, 90]):
        super().__init__(vertices, edges, inner_angles)

        if self.edges[0].lenght() != self.edges[1].lenght():
            raise ValueError("base and height are diferent, this isn't a square")
        
            
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