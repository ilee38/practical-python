# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',',
    silence_errors=False):
    """ Parse a CSV file into a list of records
    """
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        #Read the file headers
        if has_headers:
            headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = [] 

        records = []
        rownum = 0
        for row in rows:
            rownum += 1
            if not row: #Skip rows with no data
                continue
            
            try:
                # Filter the row if specific columns were selected
                if indices:
                    row = [ row[index] for index in indices]
                # Perform type conversion
                if types:
                    row = [func(val) for func, val in zip(types, row)]

                if has_headers:
                    # Make a dictionary    
                    record = dict(zip(headers, row))
                else:
                    # Make a tuple
                    record = tuple(row)

                records.append(record)
            except ValueError as e:
                if not silence_errors:
                    print(f'Row {rownum}: Couldn\'t convert {row}')
                    print(f'Row {rownum}: Reason {e}')
            continue

    return records