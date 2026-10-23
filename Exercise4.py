orders = [
    {
        "order_id": "O101",
        "customer_id": "C1",
        "status": "paid",
        "items": [
            {"sku": "A", "quantity": 2, "unit_price": 100},
            {"sku": "B", "quantity": 1, "unit_price": 50},
        ],
    },
    {
        "order_id": "O102",
        "customer_id": "C2",
        "status": "paid",
        "items": [
            {"sku": "A", "quantity": 1, "unit_price": 100},
            {"sku": "C", "quantity": 3, "unit_price": 20},
        ],
    },
    {
        "order_id": "O103",
        "customer_id": "C1",
        "status": "pending",
        "items": [
            {"sku": "B", "quantity": 2, "unit_price": 50},
        ],
    },
    {
        "order_id": "O104",
        "customer_id": "C2",
        "status": "cancelled",
        "items": [
            {"sku": "D", "quantity": 1, "unit_price": 300},
        ],
    },
    {
        "order_id": "O105",
        "customer_id": "C1",
        "status": "paid",
        "items": [
            {"sku": "A", "quantity": 1, "unit_price": 100},
            {"sku": "D", "quantity": 2, "unit_price": 300},
        ],
    },
]
# v=0
# sum=0
# l=[]
# for order in orders:

#     res = order["order_id"] 
#     for item in order["items"]:
#         v += item["quantity"]*item["unit_price"]
#         if item not in l:
#             l.append(v) 
#         v=0   
#         break     
# print(l)

for order in orders:
    order_total = 0

    for item in order["items"]:
        order_total += item["quantity"] * item["unit_price"]

    print(order["order_id"], order_total)