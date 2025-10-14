import pymysql

class DAOEmpleado:
    def connect(self):
        return pymysql.connect(host="db",user="root",password="root",db="db_poo" )

    def read(self, id):
        con = DAOEmpleado.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM empleado order by nombre asc")
            else:
                cursor.execute("SELECT * FROM empleado where id = %s order by nombre asc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,data):
        con = DAOEmpleado.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO empleado(nombre,telefono,email,direccion) VALUES(%s, %s, %s, %s)", (data['nombre'],data['telefono'],data['email'],data['direccion'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def update(self, id, data):
        con = DAOEmpleado.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE empleado set nombre = %s, telefono = %s, email = %s, direccion = %s where id = %s", (data['nombre'],data['telefono'],data['email'],data['direccion'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        con = DAOEmpleado.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM empleado where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
