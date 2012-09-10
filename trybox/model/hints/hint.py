
class HintValidationException(Exception):
    pass

class Hint(object):

    serialize = ('trybox.model.hints.Hint', ['title', 'tooltip', 'description'],)

    def __init__(self, title, tooltip, description):
        self._title = title
        self._tooltip = tooltip
        self._description = description

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def tooltip(self):
        return self._tooltip

    def validate(self, context):
        return True