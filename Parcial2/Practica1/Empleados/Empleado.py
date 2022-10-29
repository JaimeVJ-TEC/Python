class Empleado:
    def __init__(self,idempleado=None,nombre=None, direccion=None,telefono=None) -> None:
        self._idempleado = idempleado
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono 

    @property
    def idempleado(self):
        return self._idempleado
    @property
    def nombre(self):
        return self._nombre
    @property
    def direccion(self):
        return self._direccion
    @property
    def telefono(self):
        return self._telefono
   

    def __str__(self) -> str:
        return f"\nId Empleado: {self._idempleado} \nNombre: {self._nombre} \nDireccion: {self._direccion} \nTelefono: {self._telefono}\n"

