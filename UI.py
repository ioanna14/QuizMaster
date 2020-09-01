class UserInterface:
    def __init__(self):
        pass

    @staticmethod
    def input_command():
        command = input("Command: ")
        command.split(' ')
        index = command.find(' ')
        if index == -1:
            return command, []
        cmd = command[:index]
        params = command[index + 1:].split(';')
        for i in range(len(params)):
            params[i] = params[i].strip()
        return cmd, params

    @staticmethod
    def validate_command(cmd, params):
        if cmd == 'add':
            if len(params) == 7:
                return cmd, params
            else:
                raise ValueError("Bad params!!")
        elif cmd == 'create':
            if len(params) == 3:
                if params[0] in ['easy', 'medium', 'hard']:
                    return cmd, params
            else:
                raise ValueError("Bad params!!")
        elif cmd == 'start':
            if len(params) == 1:
                return cmd, params
            else:
                raise ValueError("Bad params!!")
        elif cmd == 'exit':
            return cmd, None
        else:
            raise ValueError("Bad command!!")
