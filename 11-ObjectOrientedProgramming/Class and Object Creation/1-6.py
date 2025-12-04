class Phone():
    def description(self, color, model, system):
        self.color = color
        self.model = model
        self.system = system
    
    def behaviors(self, turneon, turneoff, charged):
        self.on = turneon
        self.off = turneoff
        self.charge = charged

    