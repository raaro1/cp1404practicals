import wikipedia

search_phrase = input('Enter a search phrase: ')
while search_phrase != '':
    results = wikipedia.search(search_phrase)
    print(results)

        except PageError:
            print(f"Page id '{search_phrase}' does not match any pages. Try another id!.")
            print()
