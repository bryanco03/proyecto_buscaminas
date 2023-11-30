

class Casilla():
    def __init__(self,bomba):
        self.bomba = bomba
        self.clicked = False
        self.bandera = False

    def get_bomba(self):
        return self.bomba
    
    def get_clicked(self):
        return self.clicked 

    def get_bandera(self):
        return self.bandera
    
    def set_vecinos(self,vecinos):
        self.vecinos = vecinos
        self.set_num_alrededor()
    def set_num_alrededor(self):
        self.num_alrededor = 0
        for casilla in self.vecinos:
            if casilla.get_bomba():
                self.num_alrededor +=1


    def get_num_alrededor(self):
        return self.num_alrededor
    
    def toggle_bandera(self):
        self.bandera = not self.bandera

    def click(self):
        self.clicked=True

    def get_vecinos(self):
        return self.vecinos

    


