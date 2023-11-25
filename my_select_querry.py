import csv
from io import StringIO
class MySelectQuery:
    def __init__(self,csv_content):
        self.csv_content=csv_content
    @classmethod
    def constructor(cls,csv_content):
        instance=cls(csv_content)
        return instance 
    def where(self,column_name,value):
        # converting csv file as str to a list of dictionnary
        csv_file=StringIO(self.csv_content)
        reader=csv.DictReader(csv_file)
        list_of_dict=[]
        for row in reader:
            list_of_dict.append(dict(row))
        keys=list(list_of_dict[0].keys())##using one element of the dictionnary list to get all the dictionnary keys and converting them into a list 
        if column_name in keys:
            for i in range(len(list_of_dict)):
                if value == list_of_dict[i][column_name]:
                    result = list(list_of_dict[i].values())
                    result=[",".join(result)]
        return result     
        