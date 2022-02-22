from enum import Enum

from concrete_class.controller import Controller
from concrete_class.e_mail import Email


class InferBreachType(Enum):
    CONTROLLER = Controller()
    EMAIL = Email()
