import json

def home():
    posts = db(Post.is_draft == False).select(
        orderby=~Post.created_on,
        cache=(cache.ram, 300)
    )
    return dict(posts=posts, loginform=auth.login())





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
    logger.info("recebido mensagem em contato:" + str(request.vars))
    if request.env.request_method == "POST":
        # executo o que eu quiser
        logger.info(IS_EMAIL()(request.vars.email))
        if IS_EMAIL()(request.vars.email)[1]:
            # erro, invalido
            # ("email@xxx.com", "menasgem de erro")
            redirect(URL('home')) # HTTP(302)
        # Valido
        # ("email@xxx.com", None)
        hora = request.now.strftime("%d/%m/%Y")
        message = (
            "<html>Nova mensagem recebida:<br>"
            "Nome: %(nome)s<br>"
            "Email:%(email)s<br>"
            "Mensagem:%(mensagem)s<br>"
            "%(hora)s"
            "</html>"
            )

        mail.send(
            to=config.admin.email,
            subject="Nova mensagem recebida",
            message=message % dict(hora=hora, **request.vars)
            )

    return dict(message="Email enviado com sucesso!")

def about():
    import time
    # t = time.ctime()
    t = cache.ram('time', time.ctime, time_expire=10) 
    return str(t)

@cache('templatecache', cache_model=cache.ram, time_expire=10)
def controllercache():
    import time
    import datetime
    d = {'time': time.ctime(), 'day': datetime.datetime.now()}
    return d


@cache('templatecache', cache_model=cache.ram, time_expire=10)
def templatecache():
    import time
    import datetime
    d = {'time': time.ctime(), 'day': datetime.datetime.now()}
    # para colocar o template(view) no cache response.render
    return response.render(d)

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
