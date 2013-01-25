@auth.requires_membership("admin")
def category():
    form = SQLFORM(Category,
              formstyle="divs",
              submit_button="enviar",
              _class="admform",
              _id="formblogs")

    if form.process().accepted:
        response.flash = "Sucesso!"
    elif form.errors:
        response.flash = "Voce errou!"
    else:
        response.flash = "Preencha o formulario"
    response.view = 'manager/default.html'
    return dict(form=form)

@auth.requires_membership("admin")
def blogs():
    form = SQLFORM(Blog,
              formstyle="divs",
              submit_button="enviar",
              _class="admform",
              _id="formblogs")

    if form.process().accepted:
        response.flash = "Sucesso!"
    elif form.errors:
        response.flash = "Voce errou!"
    else:
        response.flash = "Preencha o formulario"
    response.view = 'manager/default.html'
    return dict(form=form)

@auth.requires_login()
def users():
    pass
