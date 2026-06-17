"""
## 2. Payment Methods — Duck Typing Polymorphism  *(Medium)*

=================================================
PAYMENT METHODS (DUCK TYPING)
=================================================

Problem Statement:
Build THREE INDEPENDENT classes that do NOT
share a common parent:

   class CreditCard:
       pay(amount)
   class UPI:
       pay(amount)
   class Cash:
       pay(amount)

Even though they have no common base class,
each one has a method named `pay(amount)`.
A single function `checkout(payment_method,
amount)` should work with ALL of them, just by
calling `payment_method.pay(amount)`.

This is DUCK TYPING POLYMORPHISM:
   "If it walks like a duck and quacks like a
    duck, it's a duck."
   If an object has a `pay()` method, the
   function treats it as a payment method.


-------------------------------------------------
Input Example:
methods = [
   CreditCard("Alice", "4111-1111-1111-1111"),
   UPI("bob@upi"),
   Cash("Carol"),
]

for m in methods:
    checkout(m, 500)

Output Example:
[CreditCard] Alice paid 500 via card 4111-1111-1111-1111
[UPI]        bob@upi paid 500
[Cash]       Carol paid 500 in cash

-------------------------------------------------
Explanation:
- `checkout` does not care which CLASS the
  object is, only that the object has a
  `pay()` method.
- This is polymorphism WITHOUT inheritance —
  Python doesn't require a shared base class.
- Adding a new payment method later (e.g.
  PayPal) only requires writing a new class
  with a `pay()` method; `checkout` keeps
  working unchanged.
=================================================

"""
class CreditCard:

    def _init_(self, name: str, card_number: str):
        self.name = name
        self.card_number = card_number

    def pay(self, amount: float):
        print(
            f"[CreditCard] {self.name} paid {amount} via card {self.card_number}"
        )


class UPI:

    def _init_(self, upi_id: str):
        self.upi_id = upi_id

    def pay(self, amount: float):
        print(f"[UPI]        {self.upi_id} paid {amount}")


class Cash:

    def _init_(self, name: str):
        self.name = name

    def pay(self, amount: float):
        print(f"[Cash]       {self.name} paid {amount} in cash")


def checkout(payment_method, amount: float):
    payment_method.pay(amount)

_name_ = " "
if _name_ == "_main_":
    methods = [
        CreditCard("Alice", "4111-1111-1111-1111"),
        UPI("bob@upi"),
        Cash("Carol"),
    ]
    for m in methods:
        checkout(m, 500)
