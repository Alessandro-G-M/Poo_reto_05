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
