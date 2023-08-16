meals = int(input("no. of meals: "))
snacks = int(input("no. of snacks: "))
juice = int(input("no. of juice: "))
meals_price = 100
snacks_price = 50
juice_price = 20
print("no. of meals *", meals,"=",(meals*meals_price))
print("no. of snacks *",snacks,"=",(snacks*snacks_price))
print("no of juice *",juice,"=",(juice*juice_price))
print("total amount: ", (( meals*meals_price)+(snacks*snacks_price)+(juice*juice_price)))
