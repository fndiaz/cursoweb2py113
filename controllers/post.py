def show():
    return "post"

def edit():
    return "edit post"

def delete():
    return "delete"


@auth.requires_login()
def add():
    logger.debug("executando funcao add %s" % request.vars.postid)
    
    # try:
    #     1/0
    # except Exception as e:
    #     logger.error(str(e))

    # if auth.user.is_admin:
    #     logger.warning("usuario admin acessando paagina em produ")

    return dict(form=SQLFORM(Post).process())
