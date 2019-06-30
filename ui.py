from telegram.client import Telegram
from coder import Coder
import time

SENDER = 602691119
LISTENER = 424942052
START_MESSAGE = '1111111101111111'
END_MESSAGE = '11111111'
DELAY = 0.5


class UI(Telegram):
    def __init__(self, api_id, api_hash, database_encryption_key):
        super().__init__(api_id=api_id, api_hash=api_hash, phone=input('Enter you phone number:\n'),
                         database_encryption_key=database_encryption_key)

        self.login()

    def execute(self):
        self._print_user_info()
        role = self._chose_role()
        if role is 'q':
            self.call_method('logOut').wait()
        if role is 's':
            self._send_message()
        else:
            self._recieve_message()

    def _print_user_info(self):
        user = self.get_me()
        user.wait()

        print(
            f'Logged as: {user.update["first_name"]} {user.update["last_name"]} (user id: {user.update["id"]})')

    def _chose_role(self):
        print('\nDo you want to send or recieve secret message? (s/r)')
        return input()

    def _send_message(self):
        self.chat_id = input('Enter chat id:\n')
        if (not self.chat_id):
            self.chat_id = LISTENER

        message = input('Enter message:\n')

        self._send_bits(START_MESSAGE)
        self._send_bits(Coder.encode(message))
        self._send_bits(END_MESSAGE)

    def _send_bits(self, bits):
        for bit in bits:
            print(f'Sending bit: {bit}')

            self.call_method(
                'setName', {'first_name': 'true' if bit is '1' else 'false'})
            time.sleep(DELAY)

    def _recieve_message(self):
        self.chat_id = input('Enter chat id:\n')
        if (not self.chat_id):
            self.chat_id = SENDER

        self._wait_for_start()
        print('Connection established!')
        message = ''
        while not message.endswith(END_MESSAGE):
            message += self._get_bit()

        print(f'RECIEVED: {Coder.decode(message[:-len(END_MESSAGE)])}')

    def _get_bit(self):
        start = time.time()

        user = self.call_method('getUser', {'user_id': self.chat_id})
        user.wait()

        time.sleep(DELAY + start - time.time())

        print(f"GET: {user.update['first_name']}")
        return '1' if user.update['first_name'] == 'true' else '0'

    def _wait_for_start(self):
        buffer = ''
        while not buffer.endswith(START_MESSAGE):
            buffer += self._get_bit()
