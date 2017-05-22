#!/usr/bin/env python
import xlrd, unicodedata, sys
    
interested_columns = ( 3, 7, 19, 20, 22, 23, 25)

def print_row(table, row_no):
    new_list = []
    for i in interested_columns:
	new_list.append(sh.cell(row_no, i).value);
    table.append(new_list);


def get_max_width(table, index):
    """Get the maximum width of the given column index"""
    return max([len(str(row[index])) for row in table])


def pprint_table(table):
    """Prints out a table of data, padded for alignment
    @param out: Output stream (file-like object)
    @param table: The table to print. A list of lists.
    Each row must have the same number of columns. """

    col_paddings = []

    for i in range(len(table[0])):
        col_paddings.append(get_max_width(table, i))

    for row in table:
        # rest of the cols
        for i in range(len(row)):
            print str(row[i]).rjust(col_paddings[i]+ 2),
	print 

if __name__ == "__main__":
    
    if len(sys.argv) == 2 :
	pod_no = sys.argv[1]
    else:
	# usage
        print "Usage: python Access-Excel.py <ACE-POD-number>"
	sys.exit()
	
    wb=xlrd.open_workbook("/auto/eng_ops/CNBU-lab-ops/Testbed-Info/master-worksheet.xls")
    sh= wb.sheet_by_index(1)
    table = []

    print_row(table, 0)

    for rowno in range(sh.nrows):
	cell = sh.cell(rowno, 17).value
        if cell == "ACE-POD-"+pod_no:
	    print_row(table, rowno)

    pprint_table(table);
        


