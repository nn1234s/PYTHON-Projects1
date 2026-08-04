shopname = "Snack" + " " + " Bites "
print("Welcome to",shopname)
snack_name = "Kurkure" #strdata type
price = 9.5 #float
quantity = 15 #integer data type
is_available = True #bool data type
print("snack_name : ",snack_name)
print("Datatype of snack_name : ",type(snack_name))
print("price : ",price)
print("Datatype of price : ",type(price))
print("quantity : ",quantity)
print("Datatype of quantity : ",type(quantity))
print("is_avaliable" ,is_available)
print("Datatype of is_avaliable : ",type(is_available))
total = price * quantity 
print("Total price",total)
print("Double quantity",quantity*2)
print("Discounted price",price-0.25)
print("Is price Less then 10 Rs?",price<10)
print("Is Quantity greater then 6??",quantity>6)
print("Is price exactly 9.50??",price==9.50)
print("Letters in snack name",len(snack_name))
print("Very first letter of snack name",snack_name[0])