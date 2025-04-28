class Products:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price  
        self.quantity=quantity
    def __str__(self):
        return f'{self.name} has a price of {self.price} and quantity of {self.quantity}'
class Store:
    def __init__(self):
        self.products=[]
    def display_products(self):
        for product in self.products:
            print(product)
    def add (self,name,price,quantity):
        self.products.append(Products(name,price,quantity))
        print(f'{name} has been added')
    def sell (self,name,quantity):
        for product in self.products:
            if product.name==name:
                product.quantity-=quantity        
                print(f'{product.name} has been sold')
    def search(self,name):
        for product in self.products:
            if product.name==name:
                print(product)
            else:
                print('product not found')                
class Cart:
    def __init__(self):
        self.items=[]
    def __str__(self):
        return f'{self.items} price is {self.price}'   
    def in_cart(self,name,quantity):
        if self.quantity>=quantity:
            self.items.append((name,quantity))
            print(f'{name} has been added to cart')
        else:
            print (f' only {self.quantity} available')
    def display_cart(self):
        for item in self.items:
            if not item:
                print('cart is empty')
            else:
                print(item,f'{self.quantity} has been added to cart')
                total+= self.quantity * self.price
                print(f'total is {total}')
                return total
while True:
    print('1.Add Product')
    print('2.Display Products')    
    print('3.Sell Product')
    print('4.Search Product')
    print('5.Exit')
    print('6.Cart ')
    choice=int(input('Enter your choice:'))
    if choice==1:        
        name=input('Enter name:')       
        quantity=int(input('Enter quantity:')) 
        price=int(input('Enter price:')) 
        Store.add(name,price,quantity) 
    elif choice==2:
        Store.display_products()
    elif choice==3:
        name=input('Enter name:')        
        quantity=int(input('Enter quantity:'))        
        Store.sell(name,quantity)
    elif choice==4:                              
        name=input('Enter name:')        
        Store.search(name)
    elif choice==5:                              
        break 
    elif choice==6:
        Products.display_products()
        Cart.in_cart(name,quantity)
        Cart.display_cart()

    else:
        print('Invalid choice')
