import logging
import uuid

from register_service import register


def customer_signup(name, age):
    logging.info(f"Signing up {name} with {age} years old...")
    internal_number = uuid.uuid4()
    register(name, age, internal_number)
    logging.info(f"{name} with {age} years old signed up!")
