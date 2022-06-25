import datetime
import factory

from django.contrib.auth.models import User

from users.models import Proprietario


class UserFactory(factory.django.DjangoModelFactory):

    username = factory.Sequence(lambda x: f'user{x}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@gmail.com')
    first_name = factory.Faker('name')
    password = '#SUPERsenha09'

    class Meta:
        model = User


class ProprietarioFactory(factory.django.DjangoModelFactory):

    user = factory.SubFactory(UserFactory)
    cpf = factory.Sequence(lambda x: f'789.456.123-0{x}')
    data_nascimento = factory.Faker('date_between_dates', date_start=datetime.date(1965, 1, 1),
                                    date_end=datetime.date(2005, 12, 31))
    telefone = '(89) 994619853'
    data_cadastro = factory.LazyFunction(datetime.date.today)

    class Meta:
        model = Proprietario
