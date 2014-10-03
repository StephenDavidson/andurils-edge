from faker import Faker
from podio.common.user_generator import providers

class User:
    def __init__(self):
        pass

    @staticmethod
    def create(user_type=None):
        fake = Faker()
        fake.add_provider(providers.general_provider)
        if user_type == 'US':
            fake.add_provider(providers.us.address)
            fake.add_provider(providers.us.phone_number)

        user = {
            'word': fake.word(),
            'sentence': fake.sentence(),
            'date': fake.date(),
            'url': fake.url(),
            'email': fake.email(),
            'username': fake.username(),
            'password': fake.password(),
            'security_question': '',
            'security_answer': ' '.join(fake.words()),
            'company': fake.company(),
            'first_name': 'Peter',
            'last_name': 'Parker',
            'phone': fake.phone_number(),
            'primary_address': {
                'street': fake.street_address(),
                'city': fake.city(),
                'state': fake.state(),
                'zipcode': fake.postcode(),
                'country': fake.country(),
                'country_code': fake.country_code()
            }
        }
        return user