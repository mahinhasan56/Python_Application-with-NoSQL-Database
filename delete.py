from pymongo import MongoClient
from pprint import pprint

# Choose the appropriate client
client = MongoClient()

# Connect to db
db=client.test
employee = db.employee

# Use the condition to choose the record
# and use the delete method
db.employee.delete_one({"Age":'35'})

Queryresult = employee.find_one({'Age':'35'})

pprint(Queryresult)