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
        rkg = item.plr_rkg
        nm = item.plr_name
        rtg = item.plr_rtg
        insertValues = "INSERT INTO BLKTP_PLYRSTABLE values('" + rkg + "', '" + item.plr_name + "', '" + rtg + "')"
        cursorObject.execute(insertValues)

    # Select from the players table
    queryTable = "SELECT * from BLKTP_PLYRSTABLE"
    queryResults = cursorObject.execute(queryTable)

    playerArray = []
    # Print the records in looping format
    for result in queryResults:
        # print(result)
        playerArray.append(result)

    # connectionObject.close()
    return playerArray


def selectPlayerByRtg(rtg):
    connectionObject = sqlite3.connect("BLKTP_PLYRS.db")
    cursorObject = connectionObject.cursor()

    # Select from the players table
    queryTable = "SELECT * from BLKTP_PLYRSTABLE WHERE OVR_RTG = 93"
    queryResults = cursorObject.execute(queryTable)

    playerByRtgArray = []
    # Print the records in looping format
    for result in queryResults:
        # print(result)
        playerByRtgArray.append(result)

    connectionObject.close()
    return playerByRtgArray


# capture this whole thing in a while validation, maybe
# that way i can remove the duplication in cs file, for rtgs across tms
def matchPlayers():
    myArray = []
    myArray = createPlayerTable()
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


matchPlayers()

print(selectPlayerByRtg(93))