

class Step(object):

    serialize = ('trybox.model.Step', ['title', 'tooltip', 'description', 'hints'],)

    def __init__(self, title, tooltip, description, hints=[]):
        self._title = title
        self._tooltip = tooltip
        self._description = description
        self._hints = hints

    @property
    def title(self):
        return self._title

    @property
    def tooltip(self):
        return self._tooltip

    @property
    def description(self):
        return self._description

    @property
    def hints(self):
        return self._hints

    def __getitem__(self, item):
        return self._hints[item]