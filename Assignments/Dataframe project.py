import pandas as pd

#data entities in dictionary
Data = {
    "product id" : [23, 96, 97, 15, 87],
    "name" : ["computer", "Python Workout", "Pandas Workout", "banana", "sandwich"],
    "wholesale_price" : [500, 35, 35, 0.5, 3],
    "retail_price": [1000, 75, 75, 1, 5],
    "sales" : [100, 1000, 500, 200, 300]
}

#convert dictionary to dataframe
df_Data = pd.DataFrame(Data)
print(df_Data)
print()

#calculate Total profit for each product
df_Data["net_revenue_per_product"] = (df_Data["retail_price"] - df_Data["wholesale_price" ]) * df_Data["sales"]
print(df_Data)
print()

#Total revenue from all sales
Total_revenue = df_Data["net_revenue_per_product"].sum()
print(f"Total net revenue from all sales is {Total_revenue}")
print()

#products with retail price more than twice the wholesale price
filter = df_Data.loc[df_Data["retail_price"] > (df_Data["wholesale_price"] * 2)]
print("Products with reail price more than twice the wholesale price")
print(filter)
print()

#how much did the store make from food vs. computers vs. books
Revenue_from_food = sum(df_Data.iloc[[3,4]]["net_revenue_per_product"])
print(f"Revenue from foods: {Revenue_from_food}")
print()
Revenue_from_computer = df_Data.iloc[0]["net_revenue_per_product"]
print(f"Revenue from computer: {Revenue_from_computer}")
print()
Revenue_from_books = sum(df_Data.iloc[[1,2]]["net_revenue_per_product"])
print(f"Revenue from books: {Revenue_from_books}")
print()
#new net revenue with 30% discount
df_Data["wholesale_discount"] = df_Data["wholesale_price"] * (30/100)

df_Data["new_net_revenue_per_product"] = (df_Data["retail_price"] - (df_Data["wholesale_price"] - df_Data["wholesale_discount"])) * df_Data["sales"]
print(df_Data)
print()

#Total new net revenue from all sales
Total_new_net_revenue = df_Data["new_net_revenue_per_product"].sum()
print(f"Total new net revenue from all sales is {Total_new_net_revenue}")