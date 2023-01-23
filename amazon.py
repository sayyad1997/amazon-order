class ORDER:
    items=[]
    quantities=[]
    prices=[]
    status="open"
    
    def add_item (self,name,quantity,price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total=0
        for i in range (len(self.prices)):
            total+=self.quantities[i]*self.prices[i]
        return total

    def pay(self,payment_type,security_code):
        if payment_type=="debit":
            print("processing debit payment type")
            print(f"verifing security code : {security_code}")
            self.status="paid"

        elif payment_type=="credit":
            print("processing credit payment type")
            print(f"verifing security code : {security_code}")
            self.status="paid"

        else:
            raise Exception(f"unknown payment type : {payment_type}")

class PAYMENT_PROCESSOR:
    pass

order=ORDER()
order.add_item("keyboard",1,50)
order.add_item("ssd",1,150)
order.add_item("usb cable",2,5)
print(order.total_price())
order.pay("debit","045564")
order.pay("credit","464700")


