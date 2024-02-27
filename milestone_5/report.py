import csv
import sys
from datetime import datetime
# input_month =int(input("Введiть мiсяць числом який вас цiкавить"))
# input_year =int(input("Введiть поточний рiк числом"))
def month_for_date(month:int):
   date_obj = datetime(2024,month,1)
   return date_obj

def report (file_name, month):
   data = month
   data_month = data.strftime("%B")
   total_birth = 0
   anniver = 0
   depart_dict ={}
   depart_anniver ={}
   with open(file_name, mode="r") as file:
      rid_data_empl = csv.DictReader(file)
      for row in rid_data_empl:
         for y in row:
            if y == "birth_date":
               if datetime.strptime(row[y], "%Y-%m-%d").month == data.month:
                  total_birth+=1
                  year_new = data.year - datetime.strptime(row[y], "%Y-%m-%d").year
                  if year_new % 10 == 0 or year_new % 10 == 5:
                        anniver+=1
                        for y in row:
                           if y == "department":
                              depart_keys = row[y]
                              if depart_keys in depart_anniver.keys():
                                    depart_anniver[depart_keys]+=1
                              else:
                                    depart_anniver[depart_keys]=1
                  for y in row:
                        if y == "department":
                           depart_key = row[y]
                           if depart_key in depart_dict.keys():
                              depart_dict[depart_key]+=1
                           else:
                              depart_dict[depart_key]=1                  
   print(f'python report.py database.csv {data_month} \n Report for {data_month} generated')
   print(f'--------Birthdays------- \n Total: {total_birth},\n By department:\n {depart_dict}')
   print(f'------ Anniversarie------\n Total: {anniver} \n By department:\n {depart_anniver}')


# if __name__ == '__main__':
   # input_month =int(input("Введiть мiсяць числом який вас цiкавить"))
   # input_year =int(input("Введiть поточний рiк числом"))
   file_name_real = sys.argv[1]
   input_month = sys.argv[2]
   # data_input = month_for_date(input_month)
   report(file_name_real,month_for_date(input_month))
   # report("database.csv", data_input)