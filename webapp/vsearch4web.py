from flask import Flask, render_template
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4')
def do_search() -> str:
    return str(search4letters('Miguel e Manuela', 'eiru,!'))

@app.route('/entry')
def entry_page():
    return render_template('entry.html')
    
'''A função debug permite que eu não precise ficar parando e iniciando o serviço. 
 A medida que desenvolvo ele vai tentando já exibir o resultado. '''

app.run(debug=True)
