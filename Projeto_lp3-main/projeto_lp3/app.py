from flask import Flask, render_template, request

lista_produtos = [ # cada produto é um dicionário
        { "nome": "Coca-cola", "descricao" : "mata a sede","imagem": "https://choppmaisfacil.com.br/image/cache/catalog/produtos/Refrigerantes/1648036735_1SZ-1000x1000.jpg"}, 
        { "nome": "Doritos", "descricao" : "Suja a mão", "imagem": "https://m.media-amazon.com/images/I/610trEtCQuS._AC_UF1000,1000_QL80_.jpg"},
        {  "nome": "Chocolate", "descricao" : "bom","imagem": "https://cdn.awsli.com.br/800x800/1957/1957771/produto/10935798577112288ec.jpg" }
    ]

# Jeito errado de fazer:
# from validate_docbr import CPF # importa a classe CPF
# from validate_docbr import CNPJ # importa a classe CNPJ

# Jeito correto de fazer:
from validate_docbr import CNPJ, CPF 

app = Flask("Minha App")

# rota + função

# Definição de rota
# / - home page  
@app.route("/")
def home():
    return render_template("home.html") #tem q ter esse arquivo na pasta templates
    # render templates devolve qualquer arquivo, no caso é um arquivo HTML

# /contato - página de contato 
@app.route("/contato")
def Contato():
    return render_template("contato.html")

# /produtos - pagina produtos 

@app.route("/produtos")
def produtos():
    lista_produtos = [ # cada produto é um dicionário
        { "nome": "Coca-cola", "descricao" : "mata a sede","imagem": "https://choppmaisfacil.com.br/image/cache/catalog/produtos/Refrigerantes/1648036735_1SZ-1000x1000.jpg"}, 
        { "nome": "Doritos", "descricao" : "Suja a mão", "imagem": "https://m.media-amazon.com/images/I/610trEtCQuS._AC_UF1000,1000_QL80_.jpg"},
        {  "nome": "Chocolate", "descricao" : "bom","imagem": "https://cdn.awsli.com.br/800x800/1957/1957771/produto/10935798577112288ec.jpg" }
    ]

    return render_template("produtos.html", produtos=lista_produtos) # cuidado para não repetir o nome da função na hora de criar uma lista


# criar uma página /servicos retornar "nossos serviços" (colar oq ja tem)
# página /gerar-cpf retornar cpf aleatório (usar a biblioteca do cpf que instalamos)
# página /gerar cnpj e retornar Cnpj aleatório (usar a mesma biblioteca de cima) 

@app.route("/servicos")
def servicos():
    return "<h1> Nossos serviços <h1>" # devolve HTML como STring, péssima pratica

@app.route("/termos-de-uso")
def termos():
    return render_template("termos.html")

@app.route("/politicas-de-privacidade")
def politica():
    return render_template("politicas.html")


@app.route("/como-utilizar")
def utilizar():
    return render_template("utilizar.html")


#@app.route("/cpf")
#def gerarCpf():
#    cpf = CPF() # pode colocar dentro ou fora da função
#    return cpf.generate(True)

#@app.route("/cnpj")
#def gerarCnpj():
#    cnpj = CNPJ() # objeto do tipo CNPJ
#    return cnpj.generate(True)

@app.route("/cpf")
def gcpf():
    cpf2 = cpf.generate(True)
    return render_template("cpf.html", cpf = cpf2)

@app.route("/cnpj")
def gcnpj():
    cnpj2 = cnpj.generate(True)
    return render_template("cnpj.html", cnpj = cnpj2)

# GET /produtos/cadastro devolver o form
@app.route("/produtos/cadastro") # devolve o formulario de cadastro do produto 
def cadastro_produto():
    return render_template("cadastro_produto.html")

# POST /produtos que vai lidar com os dados enviados pelo form 
# enviados pelo form
# acessar o objeto request (importar)
@app.route("/produtos", methods=['POST'])
def salvar_produto():
    # pegando os valores digitados no form que estão na request (requisição via formulário)
    nome = request.form["nome"] # o objeto request é do próprio Flask.
    descricao = request.form["descricao"]

    # Crio um novo produto (novo dicionário)
    produto = {"nome": nome, "descricao": descricao,"imagem":""}

    # Adiciona o novo porduto na lista
    lista_produtos.append(produto)

    # Devolve o template com o novo porduto
    return render_template("produtos.html", produtos=lista_produtos)
    
app.run()

# layout
# só vai mudar onde estiver o block




