class Phone():
    def description(self, color, model, system):
        self.color = color
        self.model = model
        self.system = system
    
    def behaviors(self, turnedon, turnedoff, charged):
        self.on = turnedon
        self.off = turnedoff
        self.charge = charged