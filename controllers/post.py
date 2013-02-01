from customvalidators import valida

def show():
    return "post"

def edit():
    response.view = 'manager/default.html'
    id_postagem = request.args(0)
    if not Post[id_postagem]:
        redirect(URL('posts'))
    form = SQLFORM(Post,
                   id_postagem 
                   ).process()
    return dict(form=form)

def delete():
    return "delete"

# @auth.requires_login()
# @auth.requires_membership("admin")
# @auth.requires_membership("editor")
@auth.requires(auth.has_membership("admin") or auth.has_membership("editor"))
def add():
    logger.debug("executando funcao add post")
    Post.post_body.widget = ckeditor.widget
    form = SQLFORM(Post)
    if form.process(onvalidation=valida).accepted:
        response.flash = "sucesso"

    response.view = 'manager/default.html'
    return dict(form=form)

# exemplo custom form
def add2():
    logger.debug("executando funcao add post")
    form = SQLFORM(Post)
    if form.process(onvalidation=valida).accepted:
        response.flash = "sucesso"

    return dict(form=form)


@auth.requires(auth.has_membership("admin") or auth.has_membership("editor"))
def posts():
    #
    Post.post_date.represent = lambda v: prettydate(v)
    Post.category.represent = lambda categories: ",".join([db.category[cid].name for cid in categories])
    
    Post.id.represent = lambda v: A(v, _class="btn btn-mini btn-primary", _href=URL('post', 'edit', args=v))
    
    #
    rows = db(db.post).select(orderby=~db.post.created_on)
    
    table = TABLE(_class="table table-striped bootstrap-datatable")
    columns = ['id', 'title', 'post_body', 'post_date', 'category']
    table.append(TR(*[B(col.replace('_', ' ').capitalize())  for col in columns]))
    for row in rows:
        tr = TR()
        for col in columns:
            if Post[col].represent:
                tr.append(Post[col].represent(row[col]))
            else:
                tr.append(TD(row[col]))
        table.append(tr)

    return dict(postagens=table)


def posts2():

    #
    Post.post_date.represent = lambda v: prettydate(v)
    Post.category.represent = lambda categories: ",".join([db.category[cid].name for cid in categories])
    
    Post.id.represent = lambda v: A(v, _class="btn btn-mini btn-primary", _href=URL('post', 'edit', args=v))
    
    #
    rows = db(db.post).select(orderby=~db.post.created_on)
    return dict(rows=rows) 


def example_factory():
    form = SQLFORM.factory(
           Field("email", requires=IS_EMAIL()),
           Field("receber_news", "boolean"),
           _class="teste",
           formstyle='divs'
        )
    if form.process().accepted:

        response.flash = "ok"
    return dict(form=form)
