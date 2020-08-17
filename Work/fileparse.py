# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(file_lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    """ Parse a CSV file into a list of records
    """
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    lines = csv.reader(file_lines, delimiter=delimiter)

    #Read the file headers
    if has_headers:
         headers = next(lines)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = [] 

    records = []
    rownum = 0
    for line in lines:
        rownum += 1
        if not line: #skip lines with no data
            continue
            
        try:
            # filter the line if specific columns were selected
            if indices:
                line = [ line[index] for index in indices]
             # perform type conversion
            if types:
                line = [func(val) for func, val in zip(types, line)]

            if has_headers:
                 # make a dictionary    
                record = dict(zip(headers, line))
            else:
                # make a tuple
                record = tuple(line)

            records.append(record)
        except ValueError as e:
            if not silence_errors:
                print(f'line {rownum}: couldn\'t convert {line}')
                print(f'line {rownum}: reason {e}')
            continue

    return records
