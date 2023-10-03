from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['customer']
collection = db['customer_collection']

print('customers with a name containing "an":')

found_customers = collection.find({"name":  {"$regex": "an"}})
for customer in found_customers:
    print(customer)

print()

# Update the balance of everybody with an increment os $200
collection.update_many(
    {},
    {"$inc": {"balance": 200}}
)

print('All customers with increased balance:')
for customer in collection.find():
    print(customer)

