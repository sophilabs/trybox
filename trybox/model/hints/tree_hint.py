from hint import Hint

class TreeHint(Hint):

    serialize = ('trybox.model.hints.TreeHint', [],)

    def __init__(self, title, tooltip, description):
        super(TreeHint, self).__init__(title, tooltip, description)

class CreateFileTreeHint(TreeHint):

    serialize = ('trybox.model.hints.CreateFileTreeHint', ['filename'],)

    def __init__(self, title, tooltip, description, filename):
        super(CreateFileTreeHint, self).__init__(title, tooltip, description)
        self._filename = filename

    @property
    def filename(self):
        return self._filename