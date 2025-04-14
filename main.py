import time
import SteamAccount
from tgBot import run_bot

if __name__ == '__main__':
    while True:
        print('---SteamGuard TG Bot v1.0---\n')
        print('1. Run TG bot\n2. Add account\n3. Exit\n')
        choice = input('Enter your choice: ')

        if choice == '1':
            token = input('Enter your bot token: ')
            run_bot(token)
        elif choice == '2':
            login = input('Enter Steam login: ')
            password = input('Enter Steam password: ')
            SteamAccount.add_account(login, password)
            print('Steam account added successfully!')
        elif choice == '3':
            break
        else:
            print('Invalid choice')
            time.sleep(1)
            print('\n\n\n')