class Post():

    def __init__(self, user_id, category_id, title, publication_date, image_url, content, approved, id=""):
        self.user_id = user_id
        self.categoryId = category_id
        self.title = title
        self.publicationDate = publication_date
        self.imageUrl = image_url
        self.content = content
        self.approved = approved
        if id !="":
            self.id = id