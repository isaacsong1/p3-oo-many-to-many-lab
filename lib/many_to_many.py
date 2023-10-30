class Author:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise Exception("Name must be a string")
        else:
            self._name = new_name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str):
            raise Exception("Title must be a string")
        else:
            self._title = new_title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author, self.book, self.date, self.royalties = author, book, date, royalties
        type(self).all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise Exception("Author must be of type author")
        else:
            self._author = new_author

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, new_book):
        if not isinstance(new_book, Book):
            raise Exception("Book must be of type book")
        else:
            self._book = new_book

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, new_date):
        if not isinstance(new_date, str):
            raise Exception("Date must be a string")
        else:
            self._date = new_date

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, new_royalties):
        if not isinstance(new_royalties, int):
            raise Exception("royalties must be a string")
        else:
            self._royalties = new_royalties

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

    
