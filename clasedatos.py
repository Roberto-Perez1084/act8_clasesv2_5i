class info:
    def milista(self):
        lista_nomperros=["Uziel","Emi","Carlos"]
        for x in lista_nomperros:
            print(x)
    def mitupla(self):
        tupla_raza=("Chihuahua","Rottweiler","Pug")
        for y in tupla_raza:
            print(y)
    def miconjunto(self):
        conj_color={"Rojo","Negro","Blanco"}
        for z in conj_color:
            print(z)
    def midiccionario(self):
        dic_edad={
            "Uziel":"5",
            "Emi":"60",
            "Carlos":"2"
        }
        for x,y in dic_edad.items():
            print(x,y)
datos=info()
print("listado de nombres de perros")
datos.milista()
print("tupla de razas de perros")
datos.mitupla()
print("conjunto de colores de perros")
datos.miconjunto()
print("diccionario de edades de perros")
datos.midiccionario()