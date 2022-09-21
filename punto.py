class Punto():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def cuadrante(self):
        #hay que tener en cuenta que por defecto es el 0,0
        if (self.x==0 and self.y!=0):
            print("el punto" +str(self)+ " esta en el eje x")
        if (self.x!=0 and self.y==0):
            print("el punto" +str(self)+ " esta en el eje y")
        if (self.x>0 and self.y>0):
            print("el punto" +str(self)+ " esta en el primer cuadrante")
        if (self.x>0 and self.y<0):
            print("el punto" +str(self)+ " esta en el segundo cuadrante")
        if (self.x<0 and self.y>0):
            print("el punto" +str(self)+ " esta en el tercer cuadrante cuadrante")
        if (self.x<0 and self.y<0):
            print("el punto" +str(self)+ " esta en el cuarto cuadrante")
        else:
            print("el punto" +str(self)+ " esta en el origen")

    def vector(self, vector):
        #tengase en cuenta q en este metodo me apoyo en objetos locales
        var_x = self.x - vector.x
        var_y = self.y - vector.y
        return(Punto(var_x,var_y))

#metodo optativo para el final
    
    def __str__(self):
        return "({}, {})".format( self.x, self.y )






class Rectangulo(Punto):
    import math #la clase math se utiliza para a traves de pitagoras calcular la diagonal pero yo no he encontrado manera de 
    #necesitarla o al menos eso creo
    def __init__(self,x1,x2,y1,y2):
        #Hay que tener en cuenta que los rectangulos vienen definidos por 4 ptos
        punto1 = super().__init__(self,x1,y1) #Extremo inferior izq.
        punto2 = super().__init__(self,x2,y2) #Extremo superior dcho.
        # diagonal = punto1.vector(punto2)
        punto3 = super().__init__(punto1 + self.base(),y1)
        punto4 = super().__init__(x1,punto1 + self.altura())
        self.punto1 = punto1
        self.punto2 = punto2
        self.punto3 = punto3
        self.punto4 = punto4


        

    def base(self):
        if(self.x1>self.x2):
            return-(self.x1-self.x2)
        else:
            return(self.x1-self.x2)
    def altura(self):
        if(self.y1>self.y2):
            return-(self.y1-self.y2)
        else:
            return(self.y1-self.y2)
    
    def area(self):
        return(self.base() * self.altura())
    def __str__(self):
        return "(El vector viene definido por los puntos {}, {}, {}, {})".format( self.punto1, self.punto2,self.punto3, self.punto4 )
    


print("Empieza la experimentacion:")
objeto1 = Punto(2,3)
objeto2 =Punto(5,5)
objeto3 =Punto(-3,1)
objeto4 =Punto()

print(
    "Los objetos son :" + "\n" +
        str(objeto1) + "\n" +
        str(objeto2) + "\n" +
        str(objeto3) + "\n" +
        str(objeto4)
        
            )
print(
    "Los cuadrantes son :" + "\n" +
        "el objeto " + str(objeto1) + "tiene por cuadrante: " + objeto1.cuadrante + "\n" +
        "el objeto " + str(objeto2) + "tiene por cuadrante: " + objeto2.cuadrante + "\n" +
        "el objeto " + str(objeto3) + "tiene por cuadrante: " + objeto3.cuadrante + "\n" +
        "el objeto " + str(objeto4) + "tiene por cuadrante: " + objeto4.cuadrante + "\n" 
            )
print("Vector ab  y ba :" +
    "el vector ab es : " + str(objeto1.vector(objeto2))  + "\n" +
     "el vector ba es : " + str(objeto2.vector(objeto1))  + "\n" 
)
mi_Rectangulo = Rectangulo((objeto1.x,objeto2.x,objeto1.y,objeto2.y))
print("El rectangulo es: " + "\n" +
str(mi_Rectangulo)
)
print("base del rectangulo: " + str(mi_Rectangulo.base())) 
print("altura del rectangulo: " + str(mi_Rectangulo.altura()) )
print("area del rectangulo: " + str(mi_Rectangulo.area()))

