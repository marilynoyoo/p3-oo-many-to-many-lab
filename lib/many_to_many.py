class Book:
    all_books = []

    def __init__(self, title: str):
        self.title = title
        self._contracts = []
        Book.all_books.append(self)

    def contracts(self):
        return self._contracts

    def add_contract(self, contract: 'Contract'):
        self._contracts.append(contract)

    def authors(self):
        return [contract.author for contract in self._contracts]


class Author:
    all_authors = []

    def __init__(self, name: str):
        self.name = name
        self._contracts = []
        Author.all_authors.append(self)

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book: Book, date: str, royalties: int):
        if not isinstance(book, Book):
            raise Exception("Invalid book instance")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int) or royalties < 0 or royalties > 100:
            raise Exception("Royalties must be an integer between 0 and 100")

        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        book.add_contract(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Contract:
    all_contracts = []

    def __init__(self, author: Author, book: Book, date: str, royalties: int):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int) or royalties < 0 or royalties > 100:
            raise Exception("Royalties must be an integer between 0 and 100")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date: str):
        return [contract for contract in cls.all_contracts if contract.date == date]
