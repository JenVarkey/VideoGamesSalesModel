import psycopg2
import utils as u

class VGsales:

    def __init__(self) -> None:
        self.conn = psycopg2.connect(host="localhost", database="linear_regression", user="postgres", password="Bluejay9!")

    def get_data(self, sql, params=None):
        data = []
        cur = self.conn.cursor()
        if params is None:
            cur.execute(sql)
        else:
            cur.execute(sql, params)
        header = []
        for field in cur.description:
            header.append(field[0])
        for row in cur:
            data.append(dict(zip(header, row)))
        cur.close()
        return data