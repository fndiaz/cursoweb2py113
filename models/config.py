# session

# separar pastas
#session.connect(request, response, separate=True)

# banco de dados
# dbsession = DAL('sqlite://dbsession.db')
# session.connect(request, response, dbsession)

session.connect(request, response, cookie_key="banana")

from gluon.storage import Storage

config = Storage(
        db=Storage(),
        auth=Storage(),
        mail=Storage(),
        admin=Storage()
        )

is_shell = request.global_settings.cmd_options.shell
if request.is_local or is_shell:
    config.db.uri = "sqlite://blog_dev.sqlite"
else:
    config.db.uri = "sqlite://blog_prod.sqlite"

config.db.pool_size = 10
config.db.check_reserved = ['all']

# objetos

db = DAL(**config.db)


# logging

import logging
logger = logging.getLogger("web2py.app.blog")
logger.setLevel(logging.DEBUG)

# auth

from gluon.tools import Auth, prettydate

auth = Auth(db, controller="initial", function="user")

# extender auth
auth.settings.remember_me_form = False
auth.settings.formstyle = "divs"
auth.settings.login_next = URL('initial', 'user', args=['profile'])

auth.messages.register_button = "entra ae meu"

auth.settings.registration_requires_verification = True
auth.settings.reset_password_requires_verification = True
auth.settings.registration_requires_approval = True


# auth.settings.actions_disabled = ["register"]

# email
mail = auth.settings.mailer
mail.settings.server = "logging" or "smtp.gmail.com:587"
mail.settings.sender = "admin@mysystem.com"
mail.settings.login = "username:senha" # ger_login()


## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth, filename='private/janrain.key')


def notifica(form):
    mail.send(
          to="admin@site.com",
          subject="novo usuario aguardando aprovacao",
          message=str(form.vars)
        )
    

auth.settings.register_onaccept = notifica
#auth.settings.login_onaccept = bla


# extra fields
auth.settings.extra_fields["auth_user"] = [
     Field("bio", "text", comment="Fale sobre voce"),
     Field("picture", "upload"),
     Field("newsletter", "boolean", label="quer receber newsletter?"),
     Field("gender", requires=IS_IN_SET(["Male", "Female", "Not specified"]))
]

auth.define_tables(username=False)

# generic
if request.is_local:
    response.generic_patterns = ['*']


# response
response.title = "Meu site magnifico"
response.subtitle = "O blog do sheldon"
response.meta.keywords = "chave, outra, e utra"
response.meta.description = "blog do shedon"

#admin
config.admin.email = "admin@site.com"







