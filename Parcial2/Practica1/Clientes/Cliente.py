class Cliente:
    def __init__(self,idcliente=None,nombre=None,telefono=None,horareservacion=None) -> None:
        self._idcliente = idcliente
        self._nombre = nombre
        self._telefono = telefono
        self._horareservacion = horareservacion
        

    @property
    def idcliente(self):
        return self._idcliente
    @property
    def nombre(self):
        return self._nombre
    @property
    def telefono(self):
        return self._telefono
    @property
    def horareservacion(self):
        return self._horareservacion
   

    def __str__(self) -> str:
        return f"\nId Cliente: {self._idcliente} \nNombre: {self._nombre} \nTelefono: {self._telefono} \nHora de reservacion: {self._horareservacion}\n"

