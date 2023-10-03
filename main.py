from pymongo import MongoClient

# Connect to the local MongoDB instance
client = MongoClient('localhost', 27017)

# Select the database (replace 'yourDatabaseName' with your database's name)
db = client['customer']

# Select the 'customers' collection
collection = db['customer_collection']

customer_data = {
    "name": "Sample Customer",
    "accountNumber": "12345678",
    "balance": 1000.00,
    "transactions": []
}

result = collection.insert_one(customer_data)
print(f"Inserted customer with ID: {result.inserted_id}")

# Find one customer
customer = collection.find_one({"name": "John Doe"})
print(customer)

# Find all customers with a balance greater than $500
rich_customers = collection.find({"balance": {"$gt": 2500}})
for customer in rich_customers:
    print(customer)

# Update the balance of John Doe after a deposit of $200
collection.update_one(
    {"name": "John Doe"},
    {"$inc": {"balance": 200}}
)

# Add a new transaction for John Doe indicating the deposit
collection.update_one(
    {"name": "John Doe"},
    {
        "$push": {
            "transactions": {
                "date": "2023-09-22",
                "amount": 200,
                "description": "Deposit"
            }
        }
    }
)
