# Welcome to My Select Query
***

## Task
The challange is to write a code that take csv content(as string)
and allows the user to perform "where task" to select querry from that content 
by providing a column_name and a value of that column
## Description
I create a python class that take csv content as attribute. 
Inside the class I create the methode `where(column_name,value)`.
This methode :
- convert the csv content(as string) into a list of 
dictionnary.
- Retrive the dictionnary keys inside a list and check if the column_name
macth with any keys.
in case the column_name matchs with a dictionnary key :
- The value provided is compare with the value corresponding to that key in every element
of the list of dictionnary  

## Installation
-Downlod the file
-Open it
-Delcare an instance of the MyQuerySelector and provide a csv content (as string ) to the constructor
-Apply the where methode to the instance by providing column_name and value 
-Run the code 

## Usage
```
instance=MySelectQuery.constructor("nom,prenom\nJ,judicael")
instance.where("nom","J")
```

### DJIDONOU Judicael


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
