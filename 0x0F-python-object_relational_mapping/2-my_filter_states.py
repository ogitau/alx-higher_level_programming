#!/usr/bin/python3
"""shows all the states as per the given args"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    username, password, database = argv[1], argv[2], argv[3]

    """Establish a connection to the MySQL database"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()

    query = "SELECT * FROM states WHERE name\
        LIKE '{}' ORDER BY id ASC".format(argv[4])
    cur.execute(query)
    query_results = cur.fetchall()

    for row in query_results:
        if (row[1] == argv[4]):
            print(row)

    cur.close()
    db.close()
