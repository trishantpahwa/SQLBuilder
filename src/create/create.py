import table_operations

class create:
    query = ''

    def __init__(self):
        query = ''
        
    def create_table(self, table_name, columns):
        query = ''
        query += table_operations.create + 'TABLE ' + table_name + ' ('
        for column_name, column_type in columns:
            query += column_name + ' ' + column_type + ','
        query = query.rstrip(',')
        print query
        return query


table_name = 'employees'
columns = {
    'EmployeeID': 'INT PRIMARY KEY',
    'EmployeeName': 'VARCHAR(100)',
    'EmployeeSalary': 'INT',
    'EmployeeJoined': 'DATE'
}
create_ = create()
create_.create_table('employees', columns)