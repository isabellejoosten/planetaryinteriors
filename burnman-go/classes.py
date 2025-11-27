class Layer_Homogeneous:
    def __init__(self, name, start_radius, end_radius, density):
        self.name = name
        self.start_radius = start_radius
        self.end_radius = end_radius
        self.thickness = end_radius-start_radius
        self.density = density