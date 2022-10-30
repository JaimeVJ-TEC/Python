#  Dao = Data Access Object 0   -  Martes 5 Oct 2022
from Conexion import Conexion
from Platillo import Platillo
from logger_base import log 
from CursorDelPool import CursorDelPool

class PlatilloDao:
    _SELECT  = 'SELECT * FROM platillo ORDER BY idplatillo'
    _INSERTAR = 'INSERT INTO platillo(nombre, precio, descripcion) VALUES(%s,%s,%s)' 
    _ACTUALIZAR = 'UPDATE platillo SET nombre=%s, precio=%s, descripcion=%s WHERE idplatillo=%s'
    _ELIMINAR  = 'DELETE FROM platillo WHERE idplatillo=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
                cursor.execute(cls._SELECT)
                registros = cursor.fetchall()
                platillos = []
                for r in registros:
                    platillo = Platillo(r[0],r[1],r[2],r[3])
                    platillos.append(platillo)
                return platillos

    @classmethod
    def insertar(cls,platillo):
        with CursorDelPool() as cursor:
                valores = (platillo.nombre, platillo.precio, platillo.descripcion)
                cursor.execute(cls._INSERTAR,valores)
                log.debug("Se inserto una platillo")
                return cursor.rowcount

    @classmethod
    def actualizar(cls,platillo):
        with CursorDelPool() as cursor:
                valores = (platillo.nombre, platillo.precio, platillo.descripcion, platillo.idplatillo)
                cursor.execute(cls._ACTUALIZAR,valores)
                log.debug("Se actualizo una platillo")
                return cursor.rowcount
                
    @classmethod
    def eliminar(cls,platillo):
        with CursorDelPool() as cursor:
                valores = (platillo.idplatillo,)
                cursor.execute(cls._ELIMINAR,valores)
                log.debug("Se elimino una platillo")
                return cursor.rowcount

if __name__ == "__main__":

    # Insertar
    # platillo = Platillo(nombre="Tostadas tipo siberia",precio=55,descripcion="Tostada de maiz, aguacate, pollo y crema")
    # PlatilloInsertado = PlatilloDao.insertar(platillo)
    # log.debug(f"Platillos insertadas {PlatilloInsertado}")


    #Actualizar
    # platillo = Platillo(nombre="Tacos de barbacoa", precio=90, descripcion="Tortilla de harina con fajita, salchicha cebolla y aguacate",idplatillo=5)
    # PlatilloActualizados = PlatilloDao.actualizar(platillo)
    # log.debug(f"Platillos actualizados: {PlatilloActualizados}")

    #Eliminar
    # platillo = Platillo(idplatillo=6)
    # PlatillosEliminados = PlatilloDao.eliminar(platillo)
    # log.debug(f"Platillos eliminados {PlatillosEliminados}")

    #Seleccionar
    platillos = PlatilloDao.seleccionar()
    for p in platillos:
        print(p)