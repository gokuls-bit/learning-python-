import pyjokes

def print_jokes(language='en', category='all'):
    jokes = pyjokes.get_jokes(language=language, category=category)
    if not jokes:
        print("No jokes found. Try a different category or language.")
        return
    for i, joke in enumerate(jokes, start=1):
        print(f"{i}. {joke}\n")

if __name__ == "__main__":
    # Options: language='en', 'de'; category='neutral', 'chuck', 'all'
    print_jokes(language='en', category='all')
