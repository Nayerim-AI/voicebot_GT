import wikipediaapi
import webbrowser

def search_wikipedia(query):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(query)
    if page.exists():
        print("Judul:", page.title)
        print("Isi:", page.text)
    else:
        print("Artikel tidak ditemukan.")
        
def search_youtube(query):
    query = query.replace("search youtube for", "")
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

def search_google(query):
    query = query.replace("search google for", "")
    webbrowser.open(f"https://www.google.com/search?q={query}")