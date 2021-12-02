from datetime import date, datetime, time, timedelta
from estabelecimentos.models import Servico


def get_horario_termino(data, horario, servico):
    if not isinstance(horario, time):
        horario = time.fromisoformat(horario)
    if not isinstance(data, date):
        data = date.fromisoformat(data)
    if not isinstance(servico, Servico):
        servico = Servico.objects.get(id=servico)
    duracao = servico.duracao
    data_horario = datetime(year=data.year, month=data.month,
                            day=data.day, hour=horario.hour, minute=horario.minute)
    horario_termino = data_horario + timedelta(minutes=duracao)
    return horario_termino.strftime("%H:%M")
