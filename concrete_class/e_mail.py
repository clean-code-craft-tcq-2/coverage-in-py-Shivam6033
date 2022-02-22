from abstract_class.alert_service import AlertService


class Email(AlertService):
    @classmethod
    def send_message(cls, breachType):
        recipient = "a.b@c.com"
        if breachType == 'TOO_LOW':
            print(f'To: {recipient}')
            print('Hi, the temperature is too low')
        elif breachType == 'TOO_HIGH':
            print(f'To: {recipient}')
            print('Hi, the temperature is too high')