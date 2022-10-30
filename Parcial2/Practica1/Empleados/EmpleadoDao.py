#  Dao = Data Access Object 0   -  Martes 5 Oct 2022
from Conexion import Conexion
from Empleado import Empleado
from logger_base import log 
from CursorDelPool import CursorDelPool

class EmpleadoDao:
    _SELECT  = 'SELECT * FROM empleado ORDER BY idempleado'
    _INSERTAR = 'INSERT INTO empleado(nombre, direccion,telefono) VALUES(%s,%s,%s)' 
    _ACTUALIZAR = 'UPDATE empleado SET nombre=%s, direccion=%s,telefono=%s WHERE idempleado=%s'
    _ELIMINAR  = 'DELETE FROM empleado WHERE idempleado=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
                cursor.execute(cls._SELECT)
                registros = cursor.fetchall()
                empleados = []
                for r in registros:
                    empleado = Empleado(r[0],r[1],r[2],r[3])
                    empleados.append(empleado)
                return empleados

    @classmethod
    def insertar(cls,empleado):
        with CursorDelPool() as cursor:
                valores = (empleado.nombre, empleado.direccion, empleado.telefono)
                cursor.execute(cls._INSERTAR,valores)
                log.debug("Se registro un empleado")
                return cursor.rowcount

    @classmethod
    def actualizar(cls,empleado):
        with CursorDelPool() as cursor:
                valores = (empleado.nombre, empleado.direccion, empleado.telefono, empleado.idempleado)
                cursor.execute(cls._ACTUALIZAR,valores)
                log.debug("Se actualizo un empleado")
                # return cursor.rowcount
                
    @classmethod
    def eliminar(cls,empleado):
        with CursorDelPool() as cursor:
                valores = (empleado.idempleado,)
                cursor.execute(cls._ELIMINAR,valores)
                log.debug("Se elimino un empleado")
                return cursor.rowcount

if __name__ == "__main__":

    #INSERT
    # empleado = Empleado(nombre="Juan",direccion="Jaumave #4321",telefono="8677432320")
    # EmpleadoRegistrado = EmpleadoDao.insertar(empleado)
    # log.debug(f"empleados registrados {EmpleadoRegistrado}")

    #UPDATE
    # empleado = Empleado(nombre="Pepe",direccion="Canales #3433",telefono="8677422222", idempleado=4)
    # EmpleadoActualizado = EmpleadoDao.actualizar(empleado)
    # log.debug(f"empleados actualizados: {EmpleadoActualizado}")

    #DELETE
    # empleado = Empleado(idempleado=5)
    # EmpleadoEliminado = EmpleadoDao.eliminar(empleado)
    # log.debug(f"empleados eliminados {EmpleadoEliminado}")

    #SELECT
    empleado = EmpleadoDao.seleccionar()
    for p in empleado:
        print(p)