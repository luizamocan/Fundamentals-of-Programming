
from repository import TextFileRepository
from services import Services


def test_add_sentence():
    repo=TextFileRepository("sentences.txt")
    services=Services(repo)

    services.add_sentence("Hello world")
    assert "Hello world" in repo.get_sentences()


    services.add_sentence("Hello world")
    assert repo.get_sentences().count("Hello world") == 1

    services.add_sentence("It is")
    assert "It is"  not in repo.get_sentences()

test_add_sentence()