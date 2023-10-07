from kaggle.api.kaggle_api_extended import KaggleApi
import psycopg2
import utils as u


def get_conn():
    c = psycopg2.connect(host="localhost", database="linear_regression", user="postgres", password="***")
    return c


def download_dataset():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('gregorut/videogamesales', unzip=True)


def create_vgsales_table():
    conn = get_conn()
    create_sql = u.file2string('db/tables/vgsales.sql')
    u.runsqls(conn, create_sql)
    conn.close()


def clean_table():
    insert_str = ""
    data = u.file2string('vgsales.csv')
    data = data.replace("'", " ")
    data = data.replace("N/A", 'NULL')
    data = data.replace(";", '')
    rows = data.split('\n')
    header = rows[0].split(',')
    record_counter = 0
    for row_id, row in enumerate(rows):
        if row_id > 0:  # Row 0 contains header
            fields = row.strip().split(',')
            if len(fields) == 11:  # Make sure there are no bad rows
                data = dict(zip(header, fields))
                sql = "insert into vgsales values ("
                sql += data['Rank'] + ','
                sql += "'" + data['Name'] + "',"
                sql += "'" + data['Platform'] + "',"
                sql += data['Year'] + ','
                sql += "'" + data['Genre'] + "',"
                sql += "'" + data['Publisher'] + "',"
                sql += data['NA_Sales'] + ','
                sql += data['EU_Sales'] + ','
                sql += data['JP_Sales'] + ','
                sql += data['Other_Sales'] + ','
                sql += data['Global_Sales']
                sql += ");"
                insert_str += sql
                record_counter = row_id
    print(" rows extracted from vgsales.csv file: ", record_counter)
    conn = get_conn()
    u.runsqls(conn, insert_str)
    conn.close()
    return record_counter


def main():
    download_dataset()
    create_vgsales_table()
    clean_table()


if __name__ == "__main__":
    main()
