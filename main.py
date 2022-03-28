# from asyncore import write
import csv
import json


name_1 = "Bob"
name_2 = "John"
dataNames = ["Bob", "John"]

# with open ("data.csv", "w", encoding="cp1251", newline="") as file:
#     writer = csv.writer(file, delimiter=";")
#     writer.writerow(
#         # [name_1, name_2]
#         # dataNames
#         ("User_Name", "User_adress" )
#     )

# users_data = [
#     ["user1", "address1"],
#     ["user2", "address2"],
#     ["user3", "address3"],
# ]

# for user in users_data:
#     with open("data.csv", "a", encoding="cp1251", newline="") as file:
#         writer = csv.writer(file, delimiter=";")
#         writer.writerow(user)

# user_data = [
#     ("user_name", "user_address"),
#     ["user1", "addres1"],
#     ["user2", "addres2"],
#     ["user3", "addres3"],
# ]

# with open("data.csv", "w", encoding="cp1251", newline="") as file:
#     writer = csv.writer(file, delimiter=";")
#     writer.writerows(
#         user_data
#     )

with open("data.csv", "w", encoding="cp1251", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(
        (
            "Цена",
            "Количество монет",
            "Итог",
        )
    )

with open("data.txt") as file: 
    src = json.load(file)
# print(src)

asks = src["data"]["xrp_usd"]["asks"]
print(asks)

for a in asks:
    price = a[0]
    coin_count = a[1]
    amount = price * coin_count
    print(f"[INFO] price: {price} | Coin count: {coin_count} | Amount: {amount}")

    with open("data.csv", "a", encoding="cp1251", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(
            (
                price,
                coin_count,
                amount
            )
        )