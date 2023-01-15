Products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

Prices = [30,25,40,20,20,35,45,50,35]

Last_week = [2,3,5,8,4,4,6,2,9]


#calculate the total price average of all products
def Average (Prices):
    return sum(Prices) / len(Products)
average = Average(Prices)
print("The total price average of all products = ", round(average, 2))

#create a new price list that reduces the old prices by 5 cedis
New_price_list = []
for i in range(len(Prices)):
    New_price_list.append(Prices[i] - 5)
print("New price list = ", New_price_list)

#calculate the total revenue generated from the products
Revenue_generated = []
for num1, num2 in zip(Prices, Last_week):
    Revenue_generated.append(num1 * num2)
print("Revenue generated from each product = ", Revenue_generated )
Total_revenue = sum(Revenue_generated)
print("Total revenue generated from products = ", Total_revenue)

#based on the new prices, which products are less than 30 cedis
Products_dictionary = dict(zip(Products, New_price_list))
products_extracted = { key:value for key, value in Products_dictionary.items() if value < 30 }
print("Products less than 30 cedis are ", products_extracted)
