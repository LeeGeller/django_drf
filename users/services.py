import stripe

from config import settings


def create_product(course, user):

    stripe.api_key = settings.STRIP_API_KEY
    product = stripe.Product.create(name=course, metadata={"owner": user})
    return product.id


def create_price(price, product):
    price = stripe.Price.create(
        currency="rub",
        unit_amount=price * 100,
        product_data={"name": product},
    )
    return price.id


def create_donation(course_title, user_email, price):
    product_id = create_product(course_title, user_email)
    price_id = create_price(price, product_id)

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/course/",
        line_items=[{"price": price_id, "quantity": 1}],
        mode="payment",
    )

    return product_id, session.id, session.url
