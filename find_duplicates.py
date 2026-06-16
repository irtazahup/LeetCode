def FindDuplicates(customers):
    
    sample_dict={}
    duplicate_dict={}
    
    for customer in customers:
        if customer['customer_id'] in sample_dict:
            if customer['amount'] == sample_dict[customer['customer_id']]['amount']:
                duplicate_dict[customer['customer_id']] = customer
        else:
            sample_dict[customer['customer_id']] = customer
    
    return list(duplicate_dict),list(sample_dict)

customers = [
    {
        "customer_id": 101,
        "amount": 250.50,
        "status": "completed",
        "item_count": 3
    },
    {
        "customer_id": 102,
        "amount": 15.99,
        "status": "pending",
        "item_count": 1
    },
    {
        "customer_id": 103,
        "amount": 89.00,
        "status": "completed",
        "item_count": 5
    },
    # --- DUPLICATE OF CUSTOMER 101 ---
    {
        "customer_id": 101, 
        "amount": 250.50,
        "status": "refunded",    # Different random value
        "item_count": 3
    },
    # --- DUPLICATE OF CUSTOMER 103 ---
    {
        "customer_id": 103,
        "amount": 89.00,
        "status": "completed",
        "item_count": 2          # Different random value
    }
]

print(FindDuplicates(customers))
























