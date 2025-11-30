import wikipedia
from wikipedia import DisambiguationError
from wikipedia import PageError


def search_pages():
    """Uses search phrases to search for pages in wikipedia API"""
    search_phrase = input('Enter a page title: ')
    while search_phrase != '':
        try:
            page = wikipedia.page(search_phrase)
        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
            print()


        except PageError:
            print(f"Page id '{search_phrase}' does not match any pages. Try another id!.")
            print()

        else:
            print()
            print(page.title)
            print(page.summary)
            print(page.url)

        search_phrase = input('Enter a page title: ')
    print()
    print("Thank you.")

search_pages()