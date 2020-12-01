from xlrd import open_workbook


class Arm(object):
    def __init__(self, id, name, rtg):
        self.plr_id = id
        self.plr_name = name
        self.plr_rtg = rtg

    def __str__(self):
        return ("2K Player:\n"
                "  id = {0}\n"
                "  NAME = {1}\n"
                "  RATING = {2}\n"
                .format(self.plr_id, self.plr_name, self.plr_rtg))


wb = open_workbook('2K19_Players.xlsx')
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols

    items = []

    rows = []
    for row in range(1, number_of_rows):
        values = []
        for col in range(number_of_columns):
            value = sheet.cell(row, col).value
            try:
                value = str(int(value))
            except ValueError:
                pass
            finally:
                values.append(value)
        item = Arm(*values)
        items.append(item)


def returnItems():
    return items


