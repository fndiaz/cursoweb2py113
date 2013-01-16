
Blog = db.define_table("blog",
      Field("title", notnull=True, unique=True),
      Field("description", "text")
	)


Category = db.define_table("category",
       Field("name")
	)

Post = db.define_table("post",
      Field("blog", "reference blog"), # FK
      Field("title", notnull=True),
      Field("slug"),
      Field("post_body", "text"),
      Field("post_date", "datetime"),
      Field("is_draft", "boolean"),
      Field("tags", "list:string"),
      Field("category", "list:reference category")
	)



