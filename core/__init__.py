import datetime


class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'Olá Milorde, agora são {} horas e {} minutos.'.format(now.hour, now.minute)
        return answer

    @staticmethod
    def get_date():
        now = datetime.datetime.now()
        answer = 'Olá Milorde, hoje é dia {} de {} de {}'.format(now.day, now.strftime("%B"), now.year)
        return answer