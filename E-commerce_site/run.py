from product import Product
import repo

# def prompt_float(prompt):
#     while True:
#         try:
#             return float(input(prompt))
#         except ValueError:
#             print('Please enter a valid number.')

# def prompt_int(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             print('Please enter a valid integer.')

def menu():
    option_str = '''Options are
1 - Create Product
2 - Search Product by ID
3 - Update Product
4 - Delete Product
5 - List All Products
6 - Search by Tag
7 - Exit
Your Choice:'''
    try:
        choice = int(input(option_str))
    except ValueError:
        print('Please enter a valid option.')
        return None

    if choice == 1:
        id = int(input('ID:'))
        name = input('Name:')
        description = input('Description:')
        price = float(input('Price:'))
        stock = int(input('Stock:'))
        tags = input('Tags (comma-separated):')

        old_product = repo.search_product(id)
        if old_product:
            print('ID already exists.')
        else:
            repo.add_product(Product(id=id, name=name, description=description, price=price, stock=stock, tags=tags))
            print(f'Product {name} added successfully')
    elif choice == 2:
        id = int(input('ID:'))
        product = repo.search_product(id)
        if not product:
            print('Product Not Found.')
        else:
            print(product)
    elif choice == 3:
        id = int(input('ID:'))
        product = repo.search_product(id)
        if not product:
            print('Product Not Found.')
        else:
            print(product)
            print('Leave blank to skip a field.')
            new_price = input('New Price:')
            new_stock = input('New Stock:')
            new_desc = input('New Description:')
            new_tags = input('New Tags:')
            updates = {}
            if new_price.strip(): # .strip is used to check if input is not just whitespace
                updates['price'] = float(new_price)
            if new_stock.strip():
                updates['stock'] = int(new_stock)
            if new_desc.strip():
                updates['description'] = new_desc
            if new_tags.strip():
                updates['tags'] = new_tags
            if updates:
                repo.update_product(id, **updates)
                print(f'Product {product.name} updated successfully')
            else:
                print('No updates provided.')
    elif choice == 4:
        id = int(input('ID:'))
        product = repo.search_product(id)
        if not product:
            print('Product Not Found.')
        else:
            print(product)
            if input('Are you sure to delete(y/n)?').upper() == 'Y':
                repo.delete_product(id)
                print('Product deleted successfully')
    elif choice == 5:
        products = repo.read_all_products()
        if len(products) == 0:
            print('No product exist.')
        else:
            print('List of Products:')
            for p in products:
                print(p)
    elif choice == 6:
        tag = input('Tag to search:')
        results = repo.search_by_tag(tag)
        if not results:
            print('No products found for that tag.')
        else:
            for p in results:
                print(p)
    elif choice == 7:
        print('Thank you for using the application')
    else:
        print('Invalid option. Please try again.')

    return choice

def menus():
    choice = menu()
    while choice != 7:
        choice = menu()
    print('End of application.')

if __name__ == '__main__':
    menus()
