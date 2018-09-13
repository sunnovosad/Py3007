#
# 2. Описать класс Книга. (год, название, автор) Описать метод __eq__  для сравнения
# >> book1 = Book(‘Nineteen Eighty-Four’, 1949, ‘George Orwell’)
# >> book2 = Book(‘Nineteen Eighty-Four’, 1949, ‘George Orwell’)
# >> book3 = Book(‘Над пропастью во ржи’, 1951, ‘Jerome David Salinger’)
# >>book1 == book2
# True
# >>book1 == book3
# False
# Добавить поле с отзывами и методы добавить отзыв, посмотреть все отзывы.
# >>book1.add_review(‘Cool!!’)
# >>book1.add_review(‘Not bad’)
# >>book1.show_reviews()
# 1.
# Cool!!
#
# 2.
# Not bad
#
# Литература
# https://pythonworld.ru/osnovy/obektno-orientirovannoe-programmirovanie-obshhee-predstavlenie.html

class Book:

    def __init__(self,title = 'Python for Kids     ', year = 2013, author='Jason R. Briggs', ):
        self.title = title
        self.year= year
        self.author= author
        self.review_list = []     # Добавить поле с отзывами и методы добавить отзыв, посмотреть все отзывы.

    def __str__(self):
        return f'"{self.title}" Year: {self.year} Author: {self.author}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def add_review(self, review):
        self.review_list.append(review)

    def show_all_review(self):
        #print(self.review_list)
        if self.review_list:
            count_show = 1
            print(f'Reviews for "{self.title}" book:')
            for i in self.review_list:
                print(f'{count_show}.')
                print(i + '\n')
                count_show +=1
        else:
            print ('No reviews yet for this book.')

# Checking code....

print('~' * 50)
#books _object
book_test = Book()
print('Our books here:')
print()
print(book_test)


book1 = Book('Nineteen Eighty-Four', 1949, 'George Orwell')
book2 = Book('Nineteen Eighty-Four', 1949, 'George Orwell')       # Do same review out if books is equal(the same) (-)
book3 = Book('Над пропастью во ржи', 1951, 'Jerome David Salinger')
print(book1)
print(book2)
print(book3)
print()
print('~' * 50)


#  для сравнения
print (book1 == book2)
print (book2 == book3)
print()
print('~' * 50)

# Add reviews
book_test.add_review('Good!')
book1.add_review('Cool!!')
book1.add_review('Not bad')
book1.add_review('Very-very')

# Show  reviews
book_test.show_all_review()
print('~' * 50)
book1.show_all_review()
print('~' * 50)


book3.add_review('Interestng book.')
book3.show_all_review()
print('~' * 50)
book2.show_all_review()
print('~' * 50)