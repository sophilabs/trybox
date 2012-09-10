

class Tutorial(object):

    serialize = ('trybox.model.Tutorial', ['title', 'description', 'steps'],)

    def __init__(self, title, description, steps):
        self._title = title
        self._description = description
        self._steps = steps

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def steps(self):
        return self._steps

    def __getitem__(self, item):
        return self._steps[item]