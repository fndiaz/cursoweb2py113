
from gluon.storage import Storage

config = Storage(
        db=Storage(),
        auth=Storage(),
        mail=Storage()
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




