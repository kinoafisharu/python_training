from sys import maxsize


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
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

class Person:
    def __init__(self,
                 name=None,
                 lastname=None,
                 address=None,
                 email=None,
                 email2=None,
                 email3=None,
                 mobile=None,
                 id=None,
                 homephone=None,
                 workphone=None,
                 secondphone=None,
                 all_phones_frome_home_page=None,
                 all_emails_frome_home_page=None,
                 ):
        self.name = name
        self.lastname = lastname
        self.address = address
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.mobile = mobile
        self.id = id
        self.homephone = homephone
        self.workphone = workphone
        self.secondphone = secondphone
        self.all_phones_frome_home_page = all_phones_frome_home_page
        self.all_emails_frome_home_page = all_emails_frome_home_page


    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
