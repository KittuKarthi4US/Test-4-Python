class Book:
    def __init__(self, title, author, self_borrowed):
        self.title = title
        self.author = author
        self_borrowed = False

    def borrow_book(self):
        self_borrowed = True
        print('Book was borrowed! :')

    def return_book(self):
        self_borrowed = False
        print('Book can not be borrowed.')

Book_1 = Book('The Hobbit', 'JRR Tolkien' ,'1')
Book_2 = Book('Murder Most Unladylike', 'Robin Stevenson' ,'12')
Book_3 = Book('One Piece', 'Eichiro Oda' ,'6')
Book_1.borrow_book()
Book_1.return_book()
Book_2.borrow_book()
Book_2.return_book()
Book_3.borrow_book()
Book_3.return_book()