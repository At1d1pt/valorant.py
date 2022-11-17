class Ability:
    def __init__(self, raw) -> None:
        self.raw = raw

    @property
    def slot(self):
        return self.raw['slot']

    @property
    def name(self):
        return self.raw['displayName']

    @property
    def description(self):
        return self.raw['description']

    @property
    def icon(self):
        return self.raw['displayIcon']