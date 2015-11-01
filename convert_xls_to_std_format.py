import xlrd

def load_work_book():
    workbook = xlrd.open_workbook('data_confidential/Department of Agriculture and Cooperation.xls')
    print 'Workbook loaded'

def main():
    load_work_book()

#
main()