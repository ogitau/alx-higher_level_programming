#!/usr/bin/python3
""" runs a query on MySQL retrieve
all records from the 'states' table begenning with the letter 'N' """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    username, password, database = argv[1], argv[2], argv[3]

    """Establish a connection to the MySQL database"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cur = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cur.execute(query)
    results = cur.fetchall()

    for row in results:
        if (row[1][0] == 'N'):
            print(row)

    cur.close()
    db.close()
