import wikipedia

search_phrase = input('Enter a search phrase: ')
while search_phrase != '':
    results = wikipedia.search(search_phrase)
    print(results)

    search_phrase = input('Enter a search phrase: ')
