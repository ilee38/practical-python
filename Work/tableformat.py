# tableformat.py

class TableFormatter:
    def headings(self, headers):
        ''' Emit the table headings.
        '''
        raise NotImplementedError()


    def row(self, rowdata):
        ''' Emit a single row of table data.
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    ''' Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))


    def row(self, rowdata):
        for d in rowdata:
            d = str(d)
            print(f'{d:>10s}', end=' ')
        print() 



class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format
    '''
    def headings(self, headers):
        print(','.join(headers))


    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format
    '''
    def headings(self, headers):
        header_row = '</th><th>'.join(headers)
        print(f'<tr><th>{header_row}</th></tr>')


    def row(self, rowdata):
        single_row = '</td><td>'.join(rowdata)
        print(f'<tr><td>{single_row}</td></tr>')


class FormatError(Exception):
    pass


def create_formatter(name):
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {name}')


def print_table(table_data, attr, formatter):
    formatter.headings(attr)
    for item in table_data:
        rowdata = [ getattr(item, a) for a in attr ]
        formatter.row(rowdata)








