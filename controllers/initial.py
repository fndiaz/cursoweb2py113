import json

def home():
    posts = db(db.post).select()
    return dict(posts=posts)





    # nome = "Bruno"
    # curso = "Python"
    # # if request.vars.use_tmp:
    # #     response.view = "/tmp/teste.html"
    # logger.info(request.extension)
    # logger.info(response.view)

    # response.title += " | Funcao home"
    # return dict(nome=nome, curso=curso, lista=["1", "2"])




    # executa qualquer codigo Python
    # quantos menos codigo melhor
    # lista = [{"nome":"Bruno"}, {"nome":"Hermano"}]
    # response.headers['Content-Type'] = "text/json"
    # print response.headers 
    # return json.dumps(lista)
    # args = dict(nome="Bruno",
    #                        curso="Python",
    #                        lista=["hello", "world"])


    # return response.render("/tmp/teste.html",
    #                        **args)


def contact():
    return "form"

def about():
    return "sobre o autor"

def user():
    if request.args(0) == 'register':
        db.auth_user.bio.writable = db.auth_user.bio.readable = False

    return auth()

def account():
    return dict(register=auth.register(),
                login=auth.login())

def loginsimples():
    email = request.vars.email
    senha = request.vars.senha
    if auth.login_bare(email, senha):
        redirect(URL('initial', 'user', args='profile'))
    else:
        return "ii vc nao tem acesso1"

def download():
    return response.download(request, db)
