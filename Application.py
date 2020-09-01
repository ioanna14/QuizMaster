from Service import Service
from UI import UserInterface


class Apps:
    def __init__(self, UI, Service):
        self._UI = UI
        self._Service = Service

    def start(self):
        self._Service.init_repo()
        while True:
            cmd, pms = self._UI.input_command()
            try:
                command, params = self._UI.validate_command(cmd, pms)
                if command == 'add':
                    self._Service.add(params[0], params[1], params[2], params[3], params[4], params[5], params[6])
                elif command == 'create':
                    self._Service.create(params[0], params[1], params[2])
                elif command == 'start':
                    self._Service.start(params[0])
                elif command == 'exit':
                    return
            except Exception as exception:
                print(exception.args[0])


s = Service()
ui = UserInterface()
app = Apps(ui, s)
app.start()
