class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class.")
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        magazine._articles.append(new_article)
        return new_article

    def topic_areas(self):
        return list(set(magazine.category for magazine in self.magazines()))


class Magazine:
    _all = []  

    def __init__(self, name, category):
        if not (isinstance(name, str) and 2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self.name = name
        self.category = category
        self._articles = []
        Magazine._all.append(self)

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        return [author for author in self.contributors() if sum(
            1 for article in self._articles if article.author == author) > 2]

    @classmethod
    def top_publisher(cls):
        if not cls._all:
            return None
        return max(cls._all, key=lambda magazine: len(magazine._articles))


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of the Author class.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class.")
        if not (isinstance(title, str) and 5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self.author = author
        self.magazine = magazine
        self.title = title
