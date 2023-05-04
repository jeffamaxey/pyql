import tabulate

class ObjectRegistry(object):
    """ Registry of objects by name. """

    def __init__(self, name):

        self._name = name
        self._lookup = {}

    def help(self):
        table = tabulate.tabulate(
            self._lookup.items(), headers=['Name', self._name.capitalize()]
        )
        return "Valid names are:\n\n{0}".format(table)

    def from_name(self, name):
        """ Returns an instance for the given code. """
        if name not in self._lookup:
            raise ValueError(f'Unkown name {name} in registry')
        return self._lookup[name]

    def register(self, name, calendar):
        if name not in self._lookup:
            self._lookup[name] = calendar


