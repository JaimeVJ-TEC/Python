#  Dao = Data Access Object 0   -  Martes 5 Oct 2022
from Conexion import Conexion
from Cliente import Cliente
from logger_base import log 
from CursorDelPool import CursorDelPool

class ClienteDao:
    _SELECT  = 'SELECT * FROM cliente ORDER BY idcliente'
    _INSERTAR = 'INSERT INTO cliente(nombre, telefono, horareservacion) VALUES(%s,%s,%s)' 
    _ACTUALIZAR = 'UPDATE cliente SET nombre=%s, telefono=%s, horareservacion=%s WHERE idcliente=%s'
    _ELIMINAR  = 'DELETE FROM cliente WHERE idcliente=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
                cursor.execute(cls._SELECT)
                registros = cursor.fetchall()
                clientes = []
                for r in registros:
                    cliente = Cliente(r[0],r[1],r[2],r[3])
                    clientes.append(cliente)
                return clientes

    @classmethod
    def insertar(cls,cliente):
        with CursorDelPool() as cursor:
                valores = (cliente.nombre, cliente.telefono, cliente.horareservacion)
                cursor.execute(cls._INSERTAR,valores)
                log.debug("Se registro un cliente")
                return cursor.rowcount

    @classmethod
    def actualizar(cls,cliente):
        with CursorDelPool() as cursor:
                valores = (cliente.nombre, cliente.telefono, cliente.horareservacion, cliente.idcliente)
                cursor.execute(cls._ACTUALIZAR,valores)
                log.debug("Se actualizo un cliente")
                # return cursor.rowcount
                
    @classmethod
    def eliminar(cls,cliente):
        with CursorDelPool() as cursor:
                valores = (cliente.idcliente,)
                cursor.execute(cls._ELIMINAR,valores)
                log.debug("Se elimino un cliente")
                return cursor.rowcount

if __name__ == "__main__":

    #INSERT
    # cliente = Cliente(nombre="Juan",telefono="8677432323",horareservacion=22)
    # ClienteRegistrado = ClienteDao.insertar(cliente)
    # log.debug(f"Clientes registrados {ClienteRegistrado}")

    # #UPDATE
    # cliente = Cliente(nombre="Pepe", telefono=8673333333, horareservacion=12,idcliente=1)
    # clientesActualizados = ClienteDao.actualizar(cliente)
    # log.debug(f"Clientes actualizados: {clientesActualizados}")

    # #DELETE
    # cliente = Cliente(idcliente=1)
    # ClienteEliminado = ClienteDao.eliminar(cliente)
    # log.debug(f"Clientes eliminados {ClienteEliminado}")

    #SELECT
    cliente = ClienteDao.seleccionar()
    for p in cliente:
        print(p)