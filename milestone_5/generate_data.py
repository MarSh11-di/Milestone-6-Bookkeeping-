import csv

data_employees = [
    {
        "name": "John",
        "birth_date": "1984-04-15",
        "hire_date": "2010-05-20",
        "department": "Sales"
    },
    {
        "name": "Jane",
        "birth_date": "1990-12-08",
        "hire_date": "2015-02-10",
        "department": "Finance"
    },
    {
        "name": "Alice",
        "birth_date": "1984-02-18",
        "hire_date": "2012-09-18",
        "department": "Sales"
    },
    {
        "name": "Bob",
        "birth_date": "1978-04-30",
        "hire_date": "2018-11-05",
        "department": "Engineering"
    },
    {
        "name": "Eva",
        "birth_date": "1978-02-18",
        "hire_date": "2013-07-12",
        "department": "Finance"
    }]

def write_file (file_name):
    header = ["name", "birth_date", "hire_date", "department"]

    with open("database.csv", mode="w") as file:
        data_empl = csv.DictWriter(file, fieldnames=header)
        data_empl.writeheader()
        data_empl.writerows(file_name)
write_files = write_file(data_employees)