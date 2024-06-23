import stripe

from config import settings


def create_product(course, user):

    stripe.api_key = settings.STRIP_API_KEY
    product = stripe.Product.create(name=course, metadata={"owner": user})
    return product
