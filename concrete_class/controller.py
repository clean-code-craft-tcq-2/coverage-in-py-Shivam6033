from abstract_class.alert_service import AlertService


class Controller(AlertService):
    @classmethod
    def send_message(cls, breachType):
        header = 0xfeed
        print(f'{header}, {breachType}')