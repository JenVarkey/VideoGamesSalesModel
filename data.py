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

    def get_publishers(self):
        sql = u.file2string("db/sqls/get_unique_publishers.sql")
        return self.get_data(sql)

    def get_genres(self):
        sql = u.file2string("db/sqls/get_unique_genres.sql")
        return self.get_data(sql)

    def get_platforms(self):
        sql = u.file2string("db/sqls/get_unique_platforms.sql")
        return self.get_data(sql)

    def get_sales_summary(self):
        sql = u.file2string("db/sqls/get_sales_by_region.sql")
        return self.get_data(sql)

    def get_sales_by_year(self):
        sql = u.file2string("db/sqls/get_sales_by_year.sql")
        return self.get_data(sql)

    def get_sales_details(self, publisher, genre, platform):
        params = [publisher, genre, platform]
        sql = u.file2string("db/sqls/get_details.sql")
        return self.get_data(sql, params=params)