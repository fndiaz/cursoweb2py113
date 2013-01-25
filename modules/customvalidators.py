# coding: utf-8

class IS_NOT_BAZINGA(object):
    def __init__(self, error_message="nao pode conter bazinga"):
        self.error_message = error_message

    def __call__(self, value):
        # (value, error_message) # invalido
        # (value, None) # valido
        if "bazinga" in value.strip().lower():
            return (value, self.error_message)
        else:
            return (value, None)


def valida(form):
    # usuario nao pode usar a palavra bazinga em um post
    if "bazinga" in form.vars.post_body:
        form.errors.post_body = "You cant use the word 'bazinga' in a post"
