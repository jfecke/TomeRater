class User(object):
    #
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return 'Your password has successfully been updated.'

    def __repr__(self):
        return "Name: {name}\nEmail: {email}\nBooks Read: {books}".format(name = self.name, email = self.email, books = len(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def average_rating(self):
        total = 0
        count = 0
        for i in self.books.values():
            if i is not None:
                count += 1
                total += i
        return total/count


class Book(object):
    #docstring for Book
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_number):
        self.isbn = new_number
        return 'The ISBN for ' + self.title + ' has successfully been updated.'

    def add_rating(self,rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            return 'Invalid Rating'

    def get_average_rating(self):
        total = 0
        count = 0
        for i in self.ratings:
            total += i
            count += 1
        return total/count

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    #
    def __init__(self, title, author, isbn):
        super().__init__(title,isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)

class Non_Fiction(Book):
    #
    def __init__(self, title, subject, level,isbn):
        super().__init__(title,isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return subject

    def get_level(self):
        return level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)


class TomeRater():
    #
    def __init__(self):
        self.users = {}
        self.books = {}

    def __repr__(self):
        return "This library contains {x} books and {y} users.".format(x = len(self.books), y = len(self.users))

    def create_book(self, title, isbn):
        for i in self.books:
            if isbn == i.isbn:
                return 'Sorry, {book} with an ISBN of {isbn} is already in our collection'.format(book =i.title, isbn = isbn)
        return Book(title,isbn)


    def create_novel(self, title, author, isbn):
        for i in self.books:
            if isbn == i.isbn:
                return 'Sorry, {book} with an ISBN of {isbn} is already in our collection'.format(book =i.title, isbn = isbn)
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        for i in self.books:
            if isbn == i.isbn:
                return 'Sorry, {book} with an ISBN of {isbn} is already in our collection'.format(book =i.title, isbn = isbn)
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating = None):
        if email in self.users:
            for i in self.books:
                if book.isbn == i.isbn and book.title != i.title:
                    return 'Sorry, {book} with an ISBN of {isbn} is already in our collection'.format(book =i.title, isbn = isbn)
            self.users[email].read_book(book, rating)
            if rating is not None:
                book.add_rating(rating)
            if book in self.books:
                self.books[book] +=1
            else:
                self.books[book] = 1

        else:
            return "No user with email {email}!".format(email = email)

    def add_user(self, name, email, books = None):
        
        if '@' not in email or '.com' not in email or '.edu' not in email or '.org' not in email:
            print('Please enter a valid email address')

        elif email in self.users:
            print('Sorry, a user with the email address: {email} already exists in our database. Please use a different one.'.format(email = email))
        else:

            self.users[email] = User(name, email)
            if books is not None:
                for i in books:
                    self.add_book_to_user(i, email)

    def print_catalog(self):
        print("Complete Catalog:")
        for i in self.books:
            print(i)

    def print_users(self):
        print("Users:")
        print('--------------------')
        for i in self.users:
            print(self.users[i])
            print('--------------------')

    def most_read_book(self):
        count = 0
        book = None
        for i in self.books:
            if self.books[i] > count:
                count = self.books[i]
                book = i
        print("{book} has been read the most, {x} times.".format(book = book, x = count))


    def highest_rated_book(self):
        count = 0
        i = None
        for i in self.books:
            if i.get_average_rating() > count:
                count = i.get_average_rating
                book = i
        print("{book} has the highest rating at {x}.".format(book = book, x = count))

    
    def most_positive_user(self):
        rating = 0
        person = None
        for i in self.users.values():
            if i.average_rating() > rating:
                rating = i.average_rating()
                person = i
        print("{person} is the most positive user with an average rating of {x}.".format(person = person.name, x = rating))