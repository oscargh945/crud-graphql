from conection_1 import connection

class UserCrud:

    def __init__(self) -> None:
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name varchar(100) NOT NULL,
            email varchar(100) NOT NULL,
            phone varchar(50) NOT NULL,
            password varchar(250) NOT NULL,
            is_deleted boolean DEFAULT FALSE
        );"""
        cur = connection.cursor()
        cur.execute(query)
        cur.close()

    def crear_user(self, name: str, email: str, phone: str, password: str):
        try:
            with connection.cursor() as cur:
                query="INSERT INTO users (name, email, phone, password) VALUES (%s, %s, %s, %s) RETURNING *;"
                cur.execute(query, (name, email, phone, password))
                connection.commit()
                print("Usuario creado exitosamente")
                result = cur.fetchone()

                user = { 
                    "id": result[0],
                    "name": result[1],
                    "email": result[2],
                    "phone": result[3]
                }
                return user
        except Exception as err:
            print("ocurrio un error al hacer la insertacion", err)
            return None
        

    def select_user(self, id: int):
        try:
            with connection.cursor() as cur:
                query = "SELECT * FROM users WHERE id = %s AND is_deleted = FALSE;"
                cur.execute(query, (id,))
                print("usuario encontrado")
                result = cur.fetchone()

                if result is None:
                    return None

                user = {
                    "id": result[0],
                    "name": result[1],
                    "email": result[2],
                    "phone": result[3]
                }
                return user
        except Exception as err:
            print("Ocurrió un error al buscar el usuario", err)
            raise Exception("El usuario no se encontro")


    def select_total_users(self):
        try:
            with connection.cursor() as cur:
                query = "SELECT * FROM users WHERE is_deleted = FALSE ORDER BY id ASC ;"
                cur.execute(query)
                print("usuarios encontrados")
                results = cur.fetchall()

                users = []
                for result in results:
                    user = {
                        "id": result[0],
                        "name": result[1],
                        "email": result[2],
                        "phone": result[3]
                    }
                    users.append(user)

                return users

        except Exception as err:
            print("Ocurrió un error al buscar los usuarios", err)
            return [] 
        

    def update_user(self, id: int, name: str, email: str, phone: str):
        try:
            with connection.cursor() as cur:
                query="UPDATE users SET name=%s, email=%s, phone= %s WHERE id= %s RETURNING *;"
                cur.execute(query, (name, email, phone, id))
                connection.commit()
                print("usuario actualizado")
                result = cur.fetchone()
                
                user = {
                    "id": result[0],
                    "name": result[1],
                    "email": result[2],
                    "phone": result[3]
                }
                return user
        except Exception as err:
            print("ocurrio un error al hacer la actualizacion", err)
            return None


    def delete_user(self, id: int):
        try:
            with connection.cursor() as cur:
                query="UPDATE users SET is_deleted = TRUE WHERE id=%s RETURNING *;"
                cur.execute(query, (id))
                connection.commit()
                print("usuario eliminado")
                result = cur.fetchone()

                user = {
                    "id": result[0],
                    "name": result[1],
                    "email": result[2],
                    "phone": result[3]
                }
                
            return user
        except Exception as err:
            print("ocuarrio un error al eliminar el usuario", err)
            raise Exception("usuario no encontrado")


    def select_users_pagination(self, page: int, page_size: int):
        try:
            with connection.cursor() as cur:
                offset = (page - 1) * page_size
                query = f"SELECT * FROM users WHERE is_deleted = FALSE ORDER BY id ASC OFFSET {offset} LIMIT {page_size};"
                cur.execute(query)
                print("usuarios encontrados")
                results = cur.fetchall()

                users = []
                for result in results:
                    user = {
                        "id": result[0],
                        "name": result[1],
                        "email": result[2],
                        "phone": result[3]
                    }
                    users.append(user)

                return users

        except Exception as err:
            print("Ocurrió un error al buscar los usuarios", err)
            raise Exception("Asegurate de tener suficientes usuarios para mostrarlos")

    
    def search_users(self, name: str):
        try:
            with connection.cursor() as cur:
                query ="SELECT * FROM users WHERE is_deleted = FALSE AND name LIKE %s ORDER BY name ASC"
                cur.execute(query, ('%' + name + '%',))
                print("Usuarios encontrados")
                results = cur.fetchall()

                users = []
                for result in results:
                    user = {
                        "id": result[0],
                        "name": result[1],
                        "email": result[2],
                        "phone": result[3]
                    }
                    users.append(user)

                return users

        except Exception as err:
            print("Los usuarios no se pudieron encontrar en la busqueda", err)
            raise Exception("no se encuentra ningun usuario con este nombre")
        
    
    def get_all_users(self, name: str, page: int, page_size: int):
        try:
            with connection.cursor() as cur:
                offset = (page - 1) * page_size
                query = f"SELECT * FROM users WHERE is_deleted = FALSE  AND name LIKE %s ORDER BY name ASC OFFSET {offset} LIMIT {page_size}"
                cur.execute(query, ('%' + name + '%',))
                print("Los usuarios buscados fueron encontrados y paginados")
                results = cur.fetchall()

                users = []
                for result in results:
                    user = {
                        "id": result[0],
                        "name": result[1],
                        "email": result[2],
                        "phone": result[3]
                    }
                    users.append(user)

                return users
        except Exception as err:
            print("la busqueda a fallado", err)
            raise Exception("La busqueda ha fallado junto con la paginacion")
    