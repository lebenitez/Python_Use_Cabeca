from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world from Flask!'

@app.route('/entry')
def entry_page():
    return render_template('entry.html',
                the_title='Welcome to search4letters on the web!')

@app.route('/search')
def do_search() -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
# uma outra opção para a linha acima seria vowels = set('aeiou')

    word = input("Provide a word to search for vowels: ")
    found = vowels.intersection(set(word))
    print(found)

app.run()