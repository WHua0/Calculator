'''Application'''

class App:
    '''Class App'''

    @staticmethod
    def start() -> None:
        '''App Start'''
        print('Calculator App Initiated.')
        print('Type "exit" to exit.')
        print('Would you like to add, subtract, multiply or divide?')

        while True:
            user_input = input('>>> ')
            if user_input.lower() == 'exit':
                print('Exiting Calculator App ...')
                break

            # Exit Command Reminder
            print('Unknown command.')
            print('Type "exit" to exit, or type a math operation to continue.')
