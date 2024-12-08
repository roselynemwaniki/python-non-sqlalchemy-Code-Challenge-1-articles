class Article:
    # Class to represent an article, containing attributes for author, magazine, and title.

    all = []  # Class-level attribute to store all Article instances.

    def __init__(self, author, magazine, title):
        self.author = author  # The author of the article (must be an Author object).
        self.magazine = magazine  # The magazine in which the article is published.
        self._title = title  # The title of the article (private attribute).
        Article.all.append(self)  # Add the instance to the class-level list.

    # Property to get the title.
    @property
    def title(self):
        return self._title

    # Setter to update the title with validation for string type and length.
    @title.setter
    def title(self, title):
        if title != self.title:  # Prevent setting the same title again.
            return self._title
        elif isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title

    # Property to get the author.
    @property
    def author(self):
        return self._author

    # Setter to validate that the author is an Author object.
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception  # Raise an exception if the author is not valid.
        self._author = author


class Author:
    # Class to represent an author with methods to manage articles and magazines.

    all = []  # Class-level attribute to store all Author instances.

    def __init__(self, name):
        self._name = name  # Private name attribute.
        Author.all.append(self)  # Add the instance to the class-level list.
        self.author_articles = []  # List to store the author's articles.

    # Property to get the author's name.
    @property
    def name(self):
        return self._name

    # Setter to validate and set the author's name.
    @name.setter
    def name(self, name):
        if name != self.name:  # Prevent setting the same name again.
            return self._name
        elif isinstance(name, str) and len(name) > 0:
            self._name = name

    # Method to get all articles by the author.
    def articles(self):
        return [article for article in Article.all if article.author == self]

    # Method to get unique magazines the author has contributed to.
    def magazines(self):
        unique_magazines = set([article.magazine for article in self.articles()])
        return list(unique_magazines)

    # Method to add an article written by the author.
    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise Exception  # Raise an exception if the magazine is invalid.
        self.author_articles.append(magazine)
        return Article(self, magazine, title)  # Create and return a new Article instance.

    # Method to get unique categories of magazines the author has written for.
    def topic_areas(self):
        if [magazine.category for magazine in self.author_articles] == []:
            return None
        category_set = set([magazine.category for magazine in self.author_articles])
        return list(category_set)


class Magazine:
    # Class to represent a magazine with attributes for name and category.

    all = []  # Class-level attribute to store all Magazine instances.

    def __init__(self, name, category):
        self.name = name  # Magazine name.
        self.category = category  # Magazine category.
        Magazine.all.append(self)  # Add the instance to the class-level list.

    # Property to get the magazine's name.
    @property
    def name(self):
        return self._name

    # Setter to validate and set the magazine's name.
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name

    # Property to get the magazine's category.
    @property
    def category(self):
        return self._category

    # Setter to validate and set the magazine's category.
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category

    # Method to get all articles published in the magazine.
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    # Method to get unique contributors to the magazine.
    def contributors(self):
        unique_contributors = set([article.author for article in self.articles()])
        return list(unique_contributors)

    # Method to get titles of all articles in the magazine.
    def article_titles(self):
        if [article.title for article in self.articles()] == []:
            return None
        return [article.title for article in self.articles()]

    # Method to get authors who have contributed more than one article to the magazine.
    def contributing_authors(self):
        if len([article.author for article in self.articles()]) <= 2:
            return None
        return [article.author for article in self.articles()]
