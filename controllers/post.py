from customvalidators import valida

def show():
    return "post"

def edit():
    return "edit post"

def delete():
    return "delete"

# @auth.requires_login()
# @auth.requires_membership("admin")
# @auth.requires_membership("editor")
@auth.requires(auth.has_membership("admin") or auth.has_membership("editor"))
def add():
    logger.debug("executando funcao add post")
    form = SQLFORM(Post)
    if form.process(onvalidation=valida).accepted:
        response.flash = "sucesso"

    response.view = 'manager/default.html'
    return dict(form=form)
