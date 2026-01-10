
from dummy_products import products, available_sizes

def view_products():
    print("\n========================================")
    print(" List Products")
    print("========================================")
    print("Pid\tName\t\t\tPrice\tSizes\t\t\tCategory")
    for pid, p in products.items():
        print(f"{pid}\t{p['name']}\t{p['price']}\t{p['sizes']}\t{p['category']}")

def add_products():
    print("\n========================================")
    print(" Add Products")
    print("========================================")

    add_pid = str(input("Enter Product ID: "))
    if add_pid in products:
        print(f"❌ Product ID {add_pid} already exists! Please use another ID.")
        return
    add_name = str(input("Enter Name: "))
    while True:
        price_text = input("Enter Price: ").strip()
        if price_text.isdigit():
            add_price = int(price_text)
            break
        print("Price must be a number. Try again.")

    input_sizes = str(input("Enter Sizes --> S / M / L / XL (comma-separated)) : ")).upper()
    # Split input and clean spaces
    selected_sizes = []
    for size in input_sizes.split(","):
        clean_size = size.strip()
        selected_sizes.append(clean_size)

    # Validate sizes
    all_valid = True

    for size in selected_sizes:
        if size not in available_sizes:
            all_valid = False
            break

    if not all_valid:
        print("One or more sizes are invalid")
        return
    else:
        add_category = str(input("Enter Category: "))
   
    # create new dictionary value
    new_products = {
        "name": add_name,
        "price": add_price,
        "sizes": selected_sizes,
        "category": add_category
        }

    # Add to dictionary
    products[add_pid] = new_products

    # bisa juga
    #     products[add_pid] = {
    #    "name": add_name,
    #    "price": add_price,
    #    "sizes": selected_sizes,
    #    "category": add_category
    #    }


    print("\nNew Product has been successfully Added\n")
    #show latest list of products
    view_products()

def update_products():
    print("\n========================================")
    print(" Update Products")
    print("========================================")

    pid = str(input("Enter Product ID: "))
    if pid not in products:
        print("Invalid Product ID")
        return
    
    p = products[pid] #refer to key of dic = product id
    print("\nCurrent data:")
    print(f"Name     : {p['name']}")
    print(f"Price    : {p['price']}")
    print(f"Sizes    : {p['sizes']}")
    print(f"Category : {p['category']}")

    print("\nLeave blank to keep current value.")

    updated_name = str(input("Enter New Name: "))
    if updated_name:
        p["name"] = updated_name

    updated_price = input("Enter New Price: ").strip()
    if updated_price:
        if updated_price.isdigit():
            p["price"] = int(updated_price)
    else:
        print("Price not updated.")

    updated_selected_sizes = p["sizes"]
    updated_size = str(input("Enter New Size: ")).upper().strip()
    if updated_size:
        updated_selected_sizes = []
        for s in updated_size.split(","):
            updated_clean_size = s.strip()
            if updated_clean_size:
                updated_selected_sizes.append(updated_clean_size)

    # Validate sizes
    all_valid = True

    for size in updated_selected_sizes:
        if size not in available_sizes:
            all_valid = False
            break

    if not all_valid:
        print("One or more sizes are invalid. Update cancelled for sizes")
    else:
        p["sizes"] = updated_selected_sizes
    
    updated_category = str(input("Enter New Category: "))
    if updated_category:
        p["category"] = updated_category

        
    print(f"\nProduct ID {pid} has been successfully Updated\n")
    #show latest list of products
    view_products()

def remove_products():
    print("\n========================================")
    print(" Remove Products")
    print("========================================")

    pid = str(input("Enter Product ID: "))
    if pid not in products:
        print("Invalid Product ID")
        return
    del_product = products.pop(pid, None)
    print(f"\nProduct ID {pid} has been successfully Removed\n")
    view_products()

def searchbyid():
    print("\n========================================")
    print(" Display Products By ID")
    print("========================================")

    pid = str(input("Enter Product ID: "))
    if pid not in products:
        print("Invalid Product ID")
        return
    sp = products.get(pid)
    #print(f"{search_product}")
    print("\nCurrent data:")
    print(f"Name     : {sp['name']}")
    print(f"Price    : {sp['price']}")
    print(f"Sizes    : {sp['sizes']}")
    print(f"Category : {sp['category']}")


# Main Program
def main():
    while True:
        print("\n========================================")
        print(" Idealy Wear - Product Management Admin")
        print("========================================")
        print(f'''
        List Menu :
        1. View Product
        2. Add Product
        3. Update Product 
        4. Remove  Product
        5. Exit
            ''')
        menu = int(input(f"Choose an Option : "))
        if menu == 1 :
            while True:
                print("\n========================================")
                print(" Display Product")
                print("========================================")
                print("\n")
                print("Display Option :")
                print("1. All Product")
                print("2. Search Product by ID")
                print("3. Back to Main Menu")
                view_menu = int(input("Choose an Option :  "))
                if view_menu == 1:
                    view_products()
                elif view_menu == 2:
                    searchbyid()
                elif view_menu == 3:
                    break
                else: 
                    print("❌ Please enter a valid option!")
        elif menu == 2 :
            while True:
                print("\n========================================")
                print("Add New Product")
                print("========================================")
                print("\n")
                print("Add Product Option :")
                print("1. Add Product")
                print("2. Back to Main Menu")
                add_menu = int(input("Choose an Option :  "))
                if add_menu == 1:
                    add_products()
                elif add_menu == 2:
                    break
                else: 
                    print("❌ Please enter a valid option!")
        elif menu == 3 :
            while True:
                print("\n========================================")
                print("Update Product")
                print("========================================")
                print("\n")
                print("Update Option :")
                print("1. Update Product by ID")
                print("2. Back to Main Menu")
                update_menu = int(input("Choose an Option :  "))
                if update_menu == 1:
                    update_products()
                elif update_menu == 2:
                    break
                else: 
                    print("❌ Please enter a valid option!")
        elif menu == 4 :
            while True:
                print("\n========================================")
                print("Delete Product")
                print("========================================")
                print("\n")
                print("Delete Option :")
                print("1. Delete Product by ID")
                print("2. Back to Main Menu")
                delete_menu = int(input("Choose an Option :  "))
                if delete_menu == 1:
                    remove_products()
                elif delete_menu == 2:
                    break
                else: 
                    print("❌ Please enter a valid option!")
        elif menu == 5 :
            break
        else:
            print("❌ Please enter a valid option!")
        
if __name__ == "__main__":
    main()