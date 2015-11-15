import xlrd


def build_json_from_row(row, iterator):
    next_row = iterator.next()
    if row[2] == u"Total":
        return row[5], next_row
    if next_row and next_row[2] == "":
        if row[5] == "":
            inner_json = {}
            nrow = next_row
            while nrow and (nrow[1] != "Total-" + row[1]):
                inner_json[nrow[1]], nrow = build_json_from_row(nrow, iterator)
            if nrow:
                inner_json[nrow[1]] = nrow[5]
                nrow = iterator.next()
            return inner_json, nrow
        return row[5], next_row
    else:
        inner_json = {}
        nrow = next_row
        if nrow[1] == "" :
            return get_sub_cat_total(iterator, nrow)
        while nrow and (nrow[1] != "Total-" + row[1] and nrow[5] != ""):
            inner_json[nrow[1]], nrow = get_sub_cat_total(iterator, nrow)

        if nrow:
            if nrow[5] != "":
                inner_json[nrow[1]] = nrow[5]
                nrow = iterator.next()
        return inner_json, nrow


def get_sub_cat_total(iterator, row):
    next_row = iterator.next()
    while next_row and next_row[1] == "":
        row = next_row
        next_row = iterator.next()
    return row[5], next_row


def build_json():
    json_artifact = {}
    row_iterator = get_worksheet_row()
    row = row_iterator.next()
    json_artifact[row[1]], next_row = build_json_from_row(row, row_iterator)
    while next_row:
        json_artifact[next_row[1]], next_row = build_json_from_row(next_row, row_iterator)
    print dict(json_artifact)


def main():
    build_json()


def get_worksheet_row():
    workbook = xlrd.open_workbook('data_confidential/Department of Agriculture and Cooperation.xls')
    worksheet = workbook.sheets()[0]
    # for row_num in range(11, worksheet.nrows):
    for row_num in range(11, 180):
        yield worksheet.row_values(row_num)
    yield None


main()
