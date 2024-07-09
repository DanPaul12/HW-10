restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

def add_category(menu, category, item):
        menu.update({category:item})
        print(f"{category} has been added to the menu!")
        print(menu)

def update_item(menu, category, item, price):
    menu[category][item] == price
    print(f"{item} is now {price}")

def remove_item(menu, category, item):
         menu[category].pop(item)
         print(f"{item} has been removed from {category}")

add_category(restaurant_menu, "Beverages", "Sprite")
update_item(restaurant_menu, "Main Course", "Steak", 17.99)
remove_item(restaurant_menu, "Starters", "Bruschetta")