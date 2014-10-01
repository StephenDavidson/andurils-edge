import random
import string
from faker.providers import BaseProvider


class Provider(BaseProvider):
    @classmethod
    def username(cls):
        username = 'test'
        suffix = ''.join(random.choice(string.digits) for _ in range(random.choice(range(2, 6))))
        suffix += ''.join(random.choice(string.ascii_lowercase) for _ in range(random.choice(range(2, 6))))

        return username + ''.join(random.sample(suffix, len(suffix)))

    @classmethod
    def password(cls):
        password = ''
        # At least 2 digits
        password += ''.join(random.choice(string.digits) for _ in range(random.choice(range(2, 6))))
        # At least 2 Uppercase
        password += ''.join(random.choice(string.ascii_uppercase) for _ in range(random.choice(range(2, 6))))
        # At lease 4 Lowercase
        password += ''.join(random.choice(string.ascii_lowercase) for _ in range(random.choice(range(4, 6))))
        return ''.join(random.sample(password, len(password)))