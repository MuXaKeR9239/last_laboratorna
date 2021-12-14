from pandas import DataFrame
from matplotlib import pyplot as plt
from numpy import rot90
from json import dumps

class Table:
    def __init__(self, col_titles):
        self.__data = {}
        for title in col_titles:
            self.__data[title] = []

    def load_from_file(self, file_path):
        table_file  = open(file_path, 'r', encoding='utf-8')
        raw_table   = table_file.read()
        raw_rows    = raw_table.split('\n')
        rows_count  = len(raw_rows)
        cols_titles = list(self.__data.keys())

        table_file.close()
        
        for i in range(rows_count):
            raw_row = raw_rows[i]
            row = raw_row.split(' ')
            row_items_count = len(row)

            if row_items_count != len(cols_titles):
                raise ValueError(f'Еhe number of columns must be equal to the number of their titles\n\tRow: {row}\n\tTitles: {cols_titles}')

            for i in range(row_items_count):
                item = row[i]
                title = cols_titles[i]
                self.__data[title].append(item)
    
    def print(self):
        print(self.__data)
    
    def save_excel(self, filepath):
        data_frame = DataFrame(self.__data)
        data_frame.to_excel(filepath)
    
    def save_file(self, filepath):
        table_string = self.__convert_to_string()

        fs = open(filepath, 'w', encoding='utf-8')
        fs.write(table_string)
        fs.close()
    
    def save_file_json(self, filepath):
        json_file  = open(filepath, 'w', encoding='utf-8')
        json_table = dumps(self.__data)

        json_file.write(json_table)
        json_file.close()
    
    def __convert_to_array(self):
        titles = list(self.__data.keys())
        table_array = []

        for title in titles:
            array = []
            for item in self.__data[title]:
                array.append(item)
            table_array.append(array)
        
        return table_array
    
    def __convert_to_string(self):
        table_array = rot90(self.__convert_to_array(), 3)
        table_string = ''

        for row in table_array:
            row = reversed(row)
            for item in row:
                table_string += item + ' '
            table_string = table_string[:-1] + '\n'
        table_string = table_string[:-1]

        return table_string
    
    @property
    def table(self):
        return self.__data

def show_graph(table):
    table_data = table.data
    for i in range(len(table_data)):
        if i == 0: continue
        col = table_data[i] 

def main():
    table_1 = Table((
        'Дата',
        'Код ринку',
        'Ціна картоплі',
        'Ціна капусти',
        'Ціна цибулі'
    ))

    table_1.load_from_file('tables/table_1.txt')
    #table_1.print()
    table_1.save_file('table_1.txt')
    table_1.save_excel('table_1.xlsx')

if __name__ == '__main__':
    main()
