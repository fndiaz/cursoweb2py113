from customvalidators import IS_NOT_BAZINGA

# blog
Post.blog.requires = IS_IN_DB(db, 'blog.id', "%(title)s")


# post
Post.title.requires = [IS_NOT_EMPTY(error_message=T("Esta vazio!")),
                       IS_NOT_BAZINGA(),
                       IS_NOT_IN_DB(db, 'post.title', error_message=T("title already exists"))]


Post.category.requires = IS_IN_DB(db, 'category.id', "%(name)s", multiple=True)
Post.category.widget = SQLFORM.widgets.checkboxes.widget
Post.slug.compute = lambda registro: IS_SLUG()(registro.title)[1]
