class Platillo:
    def __init__(self,idplatillo=None,nombre=None,precio=None,descripcion=None) -> None:
        self._idplatillo = idplatillo
        self._nombre = nombre
        self._precio = precio
        self._descripcion = descripcion
        

    @property
    def idplatillo(self):
        return self._idplatillo
    @property
    def nombre(self):
        return self._nombre
    @property
    def precio(self):
        return self._precio
    @property
    def descripcion(self):
        return self._descripcion
   

    def __str__(self) -> str:
        return f"\nId Platillo: {self._idplatillo} \nNombre: {self._nombre} \nPrecio: {self._precio} \nDescripcion: {self._descripcion}\n"

