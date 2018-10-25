from pymongo import MongoClient
from pprint import pprint

# Choose the appropriate client
client = MongoClient()

# Connect to db
db=client.test
employee = db.employee

# Use the condition to choose the record
# and use the update method
db.employee.update_one(
        {"Age":'67'},
        {
        "$set": {
            "Name" : "Faysal",
            "Age":"35",
            "Address":"Bangladesh Tikatuli",
        }
        }
    )

Queryresult = employee.find_one({'Age':'65'})

print(Queryresult)