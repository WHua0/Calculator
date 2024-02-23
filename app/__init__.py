'''Application'''

class App:
    '''Class App'''

    @staticmethod
    def start() -> None:
        '''App Start'''
        print('Calculator App Initiated.')
        print('Type "exit" to exit.')

        while True:
            user_input = input('>>> ')
            if user_input.lower() == 'exit':
                print('Exiting Calculator App ...')
                break

            # Exit Command Reminder
            print('Unknown command. Type "exit" to exit.')
