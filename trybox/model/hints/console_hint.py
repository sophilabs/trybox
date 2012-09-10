from hint import Hint

class ConsoleHint(Hint):

    serialize = ('trybox.model.hints.ConsoleHint', [],)

    def __init__(self, title, tooltip, description):
        super(ConsoleHint, self).__init__(title, tooltip, description)

class RunCommandConsoleHint(ConsoleHint):

    serialize = ('trybox.model.hints.RunCommandConsoleHint', ['command'],)

    def __init__(self, title, tooltip, description, command):
        super(RunCommandConsoleHint, self).__init__(title, tooltip, description)
        self._command = command

    @property
    def command(self):
        return self._command

    def validate(self, context):
        return context.run_command(self._command)