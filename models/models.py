class Group:
    def __init__(self,
                 name=None,
                 header=None,
                 footer=None,
                 ):
        self.name = name
        self.header = header
        self.footer = footer

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
