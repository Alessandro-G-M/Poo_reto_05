from Package.Shape import Shape, Line

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