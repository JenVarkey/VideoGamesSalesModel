def file2string(file_name):
    with open(file_name, 'r') as f:
        return f.read()


def runsqls(conn, sqlstring):
    cur = conn.cursor()
    sqls = sqlstring.split(';')
    for sql in sqls:
        cur.execute(sql)
    conn.commit()
    cur.close()
