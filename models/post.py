class Post():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, user_id, category_id, title, publication_date, image_url, content, approved, id=""):
        self.user_id = user_id
        self.category_id = category_id
        self.title = title
        self.publication_date = publication_date
        self.image_url = image_url
        self.content = content
        self.approved = approved
        if id !="":
            self.id = id