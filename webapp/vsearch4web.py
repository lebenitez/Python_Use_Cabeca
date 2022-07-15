#from flask import Flask, render_template, request, redirect
from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)

'''
Aqui utilizei uma função de redirecionamento, para isso tive que importar redirect do módulo flask. 
Removi para usar uma segunda forma mais performática que é a de adicionar duas rodas a mesma função
como pode ser visto logo abaixo no código de @app.route('/entry')
'''
# @app.route('/')
# def hello() -> '302':
#    return redirect('/entry')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                                the_phrase=phrase,
                                the_letters=letters,
                                the_title=title,
                                the_results=results)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                            the_title='Welcome to search4letters on the Web!')
    
'''A função debug permite que eu não precise ficar parando e iniciando o serviço. 
 A medida que desenvolvo ele vai tentando já exibir o resultado. 
 Para ativar basta colocar debug=True, para inativar remover.'''

app.run(debug=True)
