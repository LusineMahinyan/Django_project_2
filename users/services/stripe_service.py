import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_product(name: str):
    return stripe.Product.create(name=name)


def create_price(product_id: str, amount: int):
    return stripe.Price.create(
        unit_amount=amount,
        currency="usd",
        product=product_id,
    )


def create_session(price_id: str):
    return stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price": price_id,
            "quantity": 1,
        }],
        mode="payment",
        success_url="http://localhost:8000/success/",
        cancel_url="http://localhost:8000/cancel/",
    )
