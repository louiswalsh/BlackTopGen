import sqlite3
import excel_reader as er
import calculator_service as cs


def createPlayerTable():
    connectionObject = sqlite3.connect("BLKTP_PLYRS.db")
    cursorObject = connectionObject.cursor()

    # Drop any existing table with the same name
    try:
        dropTable = "drop table BLKTP_PLYRSTABLE"
        cursorObject.execute(dropTable)
    finally:
        print("")

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
    print(queryTable)
    queryResults = cursorObject.execute(queryTable)
    # print(queryResults)

    playerByRtgArray = []
    # Print the records in looping format
    for result in queryResults:
        print(result)
        playerByRtgArray.append(result)

    connectionObject.close()
    return playerByRtgArray


# capture this whole thing in a while validation, maybe
# that way i can remove the duplication in cs file, for rtgs across tms
def matchPlayers():
    myArray = []
    # print(myArray)
    # teams = cs.gen_rtg_arrays()
    # print(teams)
    #
    # team1_players = []
    # for x in teams[0]:
    #
    #     print(x)
    # for z in teams[1]:
    #     print(z)

createPlayerTable()
matchPlayers()

selectPlayerByRtg(91)