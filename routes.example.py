routers = dict(

    # base router
    BASE=dict(
        default_application='blog',
    ),

    blog=dict(
        default_controller='initial',
        default_function='home',
        functions=['home', 'contact'],
    )

)
