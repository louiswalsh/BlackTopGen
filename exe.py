import sqlite3


def createPlayerTable():
    connectionObject = sqlite3.connect("BLKTP_PLYRS.db")
    cursorObject = connectionObject.cursor()

    # Drop any existing table with the same name
    try:
        dropTable = "drop table BLKTP_PLYRSTABLE"
        cursorObject.execute(dropTable)
    finally:
        print("Table was successfully dropped, via statement: " + dropTable)

    # CREATE PLAYER TABLE
    createTable = "CREATE TABLE BLKTP_PLYRSTABLE(PLYR_NM varchar(32), OVR_RTG int)"
    cursorObject.execute(createTable)

    cursorObject.execute("select * from SQLite_master where type=\"table\"")
    tables = cursorObject.fetchall()
    print("\n\nListing tables from SQLite_master:")

    for table in tables:
        print("------------------------------------------------------")
        print("DB Object Name: %s" % (table[0]))
        print("Name of the database object: %s" % (table[1]))
        print("Table Name: %s" % (table[2]))
        print("Table position: %s" % (table[3]))
        print("SQL statement: %s" % (table[4]))
        print("------------------------------------------------------\n")

    # Read in values, FORCED
    insertValues = "INSERT INTO BLKTP_PLYRSTABLE values('LeBron James', 95)"
    cursorObject.execute(insertValues)
    insertValues = "INSERT INTO BLKTP_PLYRSTABLE values('Kevin Love', 85)"
    cursorObject.execute(insertValues)

    # Get column names, for top heirarchy
    connectionObject.row_factory = sqlite3.Row
    cursor = connectionObject.execute('select * from BLKTP_PLYRSTABLE')
    # instead of cursor.description:
    row = cursor.fetchone()
    names = row.keys()
    print(names)

    # Select from the players table
    queryTable = "SELECT * from BLKTP_PLYRSTABLE"
    queryResults = cursorObject.execute(queryTable)

    # Print the records in looping format
    for result in queryResults:
        print(result)

    connectionObject.close()
