print("Clases version 2 el constructor")
class uziel:
    def __init__(self, color, edad):
        self.color = color
        self.edad = edad
    def muerde(self):
        print("Chale el perro me mordio")
    def chatperro(self, mensaje):
        print(f"Chat perro: {mensaje}")
    def chatperra(self, mensajep):
        print(f"Chat perro: {mensajep}")
    def datos(self):
        print(f"Color: {self.color} edad: {self.edad}")
chihuas=uziel("Rojo",2)
chihuas.datos()
chihuas.muerde()
chihuas.chatperro("Hola canina")
chihuas.chatperra("Hola boby")
chihuas.chatperro("Quieres ser mi gugguu?")
chihuas.chatperra("Grrrr dame agua potable........")