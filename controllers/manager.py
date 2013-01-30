
# if not auth.has_membership("admin"):
#     redirect(URL('initial', 'home'))

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

@auth.requires_membership("admin")
def user():
    grid = SQLFORM.grid(db.auth_user)
    return dict(grid=grid)

# @auth.requires_membership("admin")
def posts():

    Post.post_date.represent = lambda v, row: prettydate(v)
    Post.category.represent = lambda categories, row: ",".join([db.category[cid].name for cid in categories])
    Post.id.represent = lambda v, row: A(v, _class="btn btn-mini btn-primary", _href=URL('post', 'edit', args=v))
    
    links = [dict(header='name',body=lambda row: A( IMG(_src="http://placehold.it/50x50") )),
    dict(header='name',body=lambda row: A( IMG(_src="http://placehold.it/50x50") ))]

    grid = SQLFORM.grid(Post.blog == 1,
        create=auth.has_membership("admin"),
        user_signature=auth.has_membership("admin"),
        editable=auth.has_membership("admin"),
        deletable=auth.has_membership("admin"),
        details=False,
        csv=True,
        links=links,
        links_placement='left')
    response.view = "manager/user.html"
    return dict(grid=grid)


def posts2():
    grid = SQLFORM.smartgrid(db.blog, linked_tables=['post'])
    response.view = "manager/user.html"
    return dict(grid=grid)
