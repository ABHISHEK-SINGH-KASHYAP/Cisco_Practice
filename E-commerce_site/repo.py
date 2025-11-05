from db_setup import session
from product import Product

def read_all_products():
    products = session.query(Product).all()
    return products

def add_product(product):
    session.add(product)
    session.commit()
    print('Product Added Successfully')

def search_product(id):
    product = session.query(Product).filter_by(id = id).first()
    return product

def update_product(id, **fields): #the **fields here allow passing variable(any) number of keyword arguments
    product = search_product(id)
    if not product:
        print('Product Not Found.')
        return
    
    for key, value in fields.items():
        if hasattr(product, key):
            setattr(product, key, value) 

    session.commit()
    print('Product Updated Successfully')

def delete_product(id):
    product = search_product(id)

    if not product:
        print('Product Not Found.')
        return

    session.delete(product)
    session.commit()
    print('Product Deleted Successfully')

def search_by_tag(tag):
    if not tag:
        return []
    # simple substring match on comma-separated tags
    return session.query(Product).filter(Product.tags.like(f'%{tag}%')).all()
