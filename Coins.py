class Rupee:
    def __init__(self, rare = False):
        self.rare = rare
        if self.rare:
            self.colour = "White"
        else:
            self.colour = "Brown"
        self.value = 1
        self.colour = "Brown"
        self.edges = 1
        self.diameter = 40
        self.thickness = 5
        self.Heads = True

    def rust(self):
        self.colour = "Green"
    def clean(self):
        self.colour = "Brown"
