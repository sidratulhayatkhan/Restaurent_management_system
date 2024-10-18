from abc import ABC
from orders import Order

class User(ABC):
    def __init__(self,name,phone,email,address) -> None:
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address

class Customer(User):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__(name, phone, email, address)
        self.cart=Order()

    def view_menu(self,restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self,restaurent,item_name,quantity):
        item=restaurent.menu.find_item(item_name)
        if item:
            if quantity>item.quantity:
                print("Item Limit Exceed.")
            else:
                item.quantity=quantity
                self.cart.add_item(item)
                print("Item Added")
        else:
            print("Item Not Found")

    def view_cart(self):
        print("**View Cart**")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price :{self.cart.total_price}")

    def pay_bill(self):
        print(f"Total {self.cart.total_price} paid succesfully ")
        self.cart.clear()
        
class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary) -> None:
        super().__init__(name, phone, email, address)
        self.age=age
        self.designation=designation
        self.salary=salary

# emp=Employee("Rahim","rahim@gmail.com",12345,"Dhaka",23,"Chef",12000)
# print(emp.name)
class Admin(User):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__(name, phone, email, address)
        

    def add_employee(self,restaurent,employee):
        restaurent.add_employee(employee)

    def view_employee(self,restaurent):
       restaurent.view_employee()

    def add_new_item(self,restaurent,item):
        restaurent.menu.add_menu_item(item)

    def delete_item(self,restaurent,item):
        restaurent.menu.remove_item(item)

    def view_menu(self,restaurent):
        restaurent.menu.show_menu()


# ad.add_employee("Shagor","shagor@gmail.com",38446657,"Khulna",21,"Chef",12000)
# mamar_res=Restaurent("Mamar Restaurent")
# mn=Menu()
# item=FoodItem("Pizza",12.45,10)
# item2=FoodItem("Burger",10,30)
# ad=Admin("Karim","1234567","karim@gmail.com","Dhaka")
# ad.add_new_item(mamar_res,item)
# ad.add_new_item(mamar_res,item2)
# mn.add_menu_item(item)
# mn.add_menu_item(item2)
# # mn.show_menu()
# # ad.view_employee()
# customer1=Customer("Rahim",2345555,"rahim@gmail.com","Dhaka")
# customer1.view_menu(mamar_res)
# item_name= input("Enter item Name: ")
# item_quantity=int(input("Enter item quantity : "))
# customer1.add_to_cart(mamar_res,item_name,item_quantity)
# customer1.view_cart()