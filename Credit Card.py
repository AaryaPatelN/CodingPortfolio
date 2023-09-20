from datetime import datetime

transactions = [
    {"amount": 100.50, "location": "New York", "time": "2023-06-20T10:15:00"},
    {"amount": 500.00, "location": "Los Angeles", "time": "2023-06-20T12:30:00"},
    {"amount": 1000.00, "location": "London", "time": "2023-06-20T15:45:00"},
    {"amount": 378.66, "location": "Vancouver", "time": "2023-07-20T15:32:00"},
    {"amount": 245.00, "location": "Miami", "time": "2023-08-20T15:23:00"},
    {"amount": 175.00, "location": "Charlotte", "time": "2023-08-20T15:16:00"}
]

# Define rules and transactions
amount_threshold = 1000.00
location_threshold = 2

suspicious_transactions = []

for transaction in transactions:
    suspicious = False

    # Rule 1: Unusually large transaction amount
    if transaction["amount"] > amount_threshold:
        suspicious = True
    
    # Rule 2: Multiple transactions from the same location within a short period
    similar_transactions = [
        t for t in transactions
        if (
            t["location"] == transaction["location"] and 
            abs((datetime.strptime(t["time"], "%Y-%m-%dT%H:%M:%S") - 
                 datetime.strptime(transaction["time"], "%Y-%m-%dT%H:%M:%S")).total_seconds()) <= 1800
        )
    ]
    
    if len(similar_transactions) > location_threshold:
        suspicious = True

    if suspicious:
        suspicious_transactions.append(transaction)

for transaction in suspicious_transactions:
    print("Suspicious transaction:")
    print("Amount:", transaction["amount"])
    print("Location:", transaction["location"])
    print("Time:", transaction["time"])
    print()
