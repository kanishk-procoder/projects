print("="*50)
print(" Kake Da Dhaba ".center(50,"-"))
print("="*50)
print("-"*50)
print("Admin page".center(50))
print("-"*50)
print("add items to the menu")
items=[]
prices=[]
dashes=[]

n = int(input("How many items to be added in menu : "))

for i in range(0,n):
    item=input("enter item : ")
    price=int(input("enter price : "))
    items.append(item)
    prices.append(price)
    dash = 48 - len(str(price)) - len(item)
    dashes.append(dash)
print("-"*50)
print("~"*50)
print("MENU".center(50))
print("~"*50)

for i in range(0,n):
    print(items[i],"-"*dashes[i],prices[i])
print("~"*50)