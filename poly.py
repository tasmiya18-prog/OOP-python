class Payment:
    def pay(self):
        print("Generic payment method")

class GooglePay(Payment):
    def pay(self):
        print("Paying using Google Pay")

class PhonePe(Payment):
    def pay(self):
        print("Paying using Phone Pe")

class CreditCard(Payment):
    def pay(self):
        print("Paying using Credit card")

payment=Payment()
google_pay=GooglePay()
phone_pe=PhonePe()
credit_card=CreditCard()

payment.pay()
google_pay.pay()
phone_pe.pay()
credit_card.pay()
