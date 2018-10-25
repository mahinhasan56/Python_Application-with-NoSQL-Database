from pymongo import MongoClient
from pprint import pprint

client = MongoClient()

db=client.test

employee = db.employee
employee_details = {
    'Name': 'Mahin Hasan',
    'Address': 'Vietnam, Hanoy',
    'Age': '35',
}

result = employee.insert_one(employee_details)

Queryresult = employee.find_one({'Age': '42'})
pprint(Queryresult)