def triangle (row , defl={'R' , 'B' , 'G'}):
    row = row.replace (' ' , '')

    if len (row) == 1: return row
    if len(set(row)) == 1: return ''.join(set(row))
    row_out = ''
    for num in range (len (row) - 1):
        if row[ num ] == row[ num + 1 ]: row_out += row[ num ]
        else: row_out += ''.join ((defl - set ([ row[ num ] , row[ num + 1 ] ])))
    op = triangle (row_out)
    if op: return op