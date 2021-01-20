from config import mysql


class DepartmentModel(object):

    @staticmethod
    def get_all_departments() -> list:
        dep_list = []
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM departments ORDER BY id')
        for row in cursor.fetchall():
            dep_list.append({
                'id': row[0],
                'name': row[1]
            })
        return dep_list

    @staticmethod
    def get_name_by_id(id: int) -> str:
        query = 'select name from departments where id=%s'
        cursor = mysql.get_db().cursor()
        cursor.execute(query, (id,))
        row = cursor.fetchone()
        return row[0]
