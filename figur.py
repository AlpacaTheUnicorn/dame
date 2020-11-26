class Figur():
    def __init__(self, dame, coords):
        self.dame = dame
        self.coords = coords

    def get_d(self):
        return self.dame
    
    def set_d(self, x):
        self.dame = x
    
    def get_coords(self):
        return self.coords

    def set_coords(self, x):
        self.coords = x
    
        
