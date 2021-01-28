class User():

    def __init__(self, id, first_name, last_name, email, password = "", bio, user_name, 
                profile_image_url, created_on, active, account_type_id): 
        self.id = id
        self.firstName = first_name
        self.lastName = last_name
        self.email = email
        self.password = password
        self.bio = bio
        self.userName = user_name
        self.profileImageUrl = profile_image_url
        self.createdOn = created_on
        self.active = active
        self.accountTypeId = account_type_id
        
