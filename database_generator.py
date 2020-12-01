import sqlite3
import excel_reader as er
import calculator_service as cs
from random import randint


def createPlayerTable():
    connectionObject = sqlite3.connect("BLKTP_PLYRS.db")
    cursorObject = connectionObject.cursor()

    # Drop any existing table with the same name
    try:
        dropTable = "drop table BLKTP_PLYRSTABLE"
        cursorObject.execute(dropTable)
    finally:
        pass

    # CREATE PLAYER TABLE
    createTable = "CREATE TABLE BLKTP_PLYRSTABLE(PLYR_RKG int, PLYR_NM varchar(32), OVR_RTG int)"
    cursorObject.execute(createTable)

    # HIT EXCEL READER AND PUT INTO TABLE, ONE BY ONE
    items = er.returnItems()
    for item in items:
        id = item.plr_id
        nm = item.plr_name
        rtg = item.plr_rtg
        insertValues = "INSERT INTO BLKTP_PLYRSTABLE values('" + id + "', '" + item.plr_name + "', '" + rtg + "')"
        # print(insertValues)
        cursorObject.execute(insertValues)

    connectionObject.commit()
    # Select from the players table


def selectPlayerByRtg(rtg):
    connectionObject = sqlite3.connect("BLKTP_PLYRS.db")
    cursorObject = connectionObject.cursor()

    # Select from the players table
    queryTable = "SELECT * from BLKTP_PLYRSTABLE WHERE OVR_RTG = " + str(rtg)
    queryResults = cursorObject.execute(queryTable)
    # print(queryResults)

    player_by_rtg_array = []
    # Print the records in looping format
    for result in queryResults:
        # print(result)
        player_by_rtg_array.append(result)

    connectionObject.close()
    value = randint(0, len(player_by_rtg_array) - 1)
    print("Player: ", player_by_rtg_array[value][1], " ||  Rating: ", player_by_rtg_array[value][2])






createPlayerTable()
