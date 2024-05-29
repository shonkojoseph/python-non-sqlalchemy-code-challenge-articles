import pytest
from classes.many_to_many import Article, Magazine, Author


@pytest.fixture
def author():
    return Author("Carry Bradshaw")

@pytest.fixture
def author_2():
    return Author("Nathaniel Hawthorne")

@pytest.fixture
def magazine_1():
    return Magazine("Vogue", "Fashion")

@pytest.fixture
def magazine_2():
    return Magazine("AD", "Architecture & Design")


class TestArticle:
    """Article in many_to_many.py"""

    def test_has_title(self, author, magazine_1):
        """Article is initialized with a title"""
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author, magazine_1, "Dating life in NYC")

        assert article_1.title == "How to wear a tutu with style"
        assert article_2.title == "Dating life in NYC"

    def test_title_is_immutable_str(self, author, magazine_1):
        """title is an immutable string"""
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")

        with pytest.raises(AttributeError):
            article_1.title = 500
        
        assert isinstance(article_1.title, str)

    def test_title_is_valid(self, author, magazine_1):
        """title is between 5 and 50 characters inclusive"""
        valid_article = Article(author, magazine_1, "How to wear a tutu with style")

        assert 5 <= len(valid_article.title) <= 50

        with pytest.raises(ValueError):
            Article(author, magazine_1, "Test")

        with pytest.raises(ValueError):
            Article(author, magazine_1, "How to wear a tutu with style and walk confidently down the street")

    def test_has_an_author(self, author, author_2, magazine_1):
        """article has an author"""
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author_2, magazine_1, "Dating life in NYC")

        assert article_1.author == author
        assert article_2.author == author_2

    def test_author_of_type_author_and_mutable(self, author, author_2, magazine_1):
        """author is of type Author and mutable"""
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author_2, magazine_1, "Dating life in NYC")

        assert isinstance(article_1.author, Author)
        assert isinstance(article_2.author, Author)
        
        article_1.author = author_2
        assert isinstance(article_1.author, Author)
        assert article_1.author.name == "Nathaniel Hawthorne"

    def test_has_a_magazine(self, author, magazine_1, magazine_2):
        """article has a magazine"""
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author, magazine_2, "Dating life in NYC")

        assert article_1.magazine == magazine_1
        assert article_2.magazine == magazine_2

    def test_magazine_of_type_magazine_and_mutable(self, author, magazine_1, magazine_2):
        """magazine is of type Magazine and mutable"""
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author, magazine_2, "Dating life in NYC")

        assert isinstance(article_1.magazine, Magazine)
        assert isinstance(article_2.magazine, Magazine)
        
        article_1.magazine = magazine_2
        assert isinstance(article_1.magazine, Magazine)
        assert article_1.magazine.name == "AD"

    def test_get_all_articles(self, author, magazine_1, magazine_2):
        """Article class has all attribute"""
        Article.all = []
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author, magazine_2, "Dating life in NYC")

        assert len(Article.all) == 2
        assert article_1 in Article.all
        assert article_2 in Article.all

