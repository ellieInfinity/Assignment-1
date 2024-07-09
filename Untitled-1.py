def read_product_data(file_path):
    products = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(', ')
                products.append({
                    'ID': int(parts[0]),
                    'Name': parts[1],
                    'Price': float(parts[2]),
                    'Category': parts[3]
                })
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    return products

def write_product_data(file_path, products):
    try:
        with open(file_path, 'w') as file:
            for product in products:
                file.write(f"{product['ID']}, {product['Name']}, {product['Price']}, {product['Category']}\n")
    except Exception as e:
        print(f"An error occurred while writing to {file_path}: {e}")

def bubble_sort_by_price(products):
    n = len(products)
    for i in range(n):
        for j in range(0, n-i-1):
            if products[j]['Price'] > products[j+1]['Price']:
                products[j], products[j+1] = products[j+1], products[j]
    return products

def add_product(products, new_product):
    products.append(new_product)

def modify_product(products, product_id, updated_product):
    for product in products:
        if product['ID'] == product_id:
            product.update(updated_product)
            return True
    return False

def delete_product(products, product_id):
    for i, product in enumerate(products):
        if product['ID'] == product_id:
            del products[i]
            return True
    return False

def search_products(products, key, value):
    if key == 'ID':
        return [product for product in products if product[key] == int(value)]
    elif key == 'Price':
        return [product for product in products if product[key] == float(value)]
    else:
        return [product for product in products if value.lower() in product[key].lower()]

def main():
    file_path = 'product_data.txt'
    products = read_product_data(file_path)

    while True:
        print("\nOptions:")
        print("1. Display products")
        print("2. Add product")
        print("3. Modify product")
        print("4. Delete product")
        print("5. Search product")
        print("6. Sort products by price")
        print("7. Save and exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            for product in products:
                print(product)
        elif choice == '2':
            new_product = {
                'ID': int(input("Enter product ID: ")),
                'Name': input("Enter product name: "),
                'Price': float(input("Enter product price: ")),
                'Category': input("Enter product category: ")
            }
            add_product(products, new_product)
        elif choice == '3':
            product_id = int(input("Enter the product ID to modify: "))
            updated_product = {}
            updated_product['Name'] = input("Enter new product name (leave blank to keep current): ")
            updated_product['Price'] = input("Enter new product price (leave blank to keep current): ")
            updated_product['Category'] = input("Enter new product category (leave blank to keep current): ")
            
            updated_product = {k: v for k, v in updated_product.items() if v}
            
            if modify_product(products, product_id, updated_product):
                print("Product updated successfully.")
            else:
                print("Product not found.")
        elif choice == '4':
            product_id = int(input("Enter the product ID to delete: "))
            if delete_product(products, product_id):
                print("Product deleted successfully.")
            else:
                print("Product not found.")
        elif choice == '5':
            search_key = input("Enter the search key (ID, Name, Price, Category): ").title()
            search_value = input("Enter the search value: ")
            
            results = search_products(products, search_key, search_value)
            if results:
                for result in results:
                    print(result)
            else:
                print("No matching products found.")
        elif choice == '6':
            products = bubble_sort_by_price(products)
            for product in products:
                print(product)
        elif choice == '7':
            write_product_data(file_path, products)
            print("Products saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
