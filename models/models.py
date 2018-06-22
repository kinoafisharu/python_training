class Group:
    def __init__(self,
                 name=None,
                 header=None,
                 footer=None,
                 id=None,
                 ):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name


class Person:
    def __init__(self,
                 name=None,
                 lastname=None,
                 address=None,
                 email=None,
                 mobile=None,
                 ):
        self.name = name
        self.lastname = lastname
        self.address = address
        self.email = email
        self.mobile = mobile

