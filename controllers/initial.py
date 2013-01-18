def home():
    return "Welcome to my blog"

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
