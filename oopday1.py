class Instagram:
    def _init_(self, title, description, creator_name, location):
        # Initialize Instagram reel attributes
        self.title = title
        self.description = description
        self.creator_name = creator_name
        self.location = location
        self.likes = 0
        self.comments = []  # List to store comments

    def display_title(self):
        # Display the title of the reel
        print("The title of the reel is ", self.title)

    def display_description(self):
        # Display the description of the reel
        print("The description of the reel is ", self.description)

    def display_likes(self):
        # Display the likes of the reel
        print("The likes of the reel is ", self.likes)

    def display_creator_name(self):
        # Display the creator name of the reel
        print("The creator name of the reel is ", self.creator_name)

    def display_location(self):
        # Display the location of the reel
        print("The location of the reel is ", self.location)

    def display_comments(self):
        # Display the comments of the reel
        print("The comments of the reel are: ")
        for comment in self.comments:
            print(comment)

    def liked(self):
        # Increment the likes of the reel
        self.likes += 1

    def disliked(self):
        # Decrement the likes of the reel if it's greater than 0
        if self.likes > 0:
            self.likes -= 1

    def add_comment(self, comment):
        # Add a comment to the reel
        self.comments.append(comment)

reel1 = Instagram("dancing", "dancing with friends", "John Doe", "New York")
reel1.disliked()  # 0
reel1.liked()  # 1
reel2 = Instagram("finance minister conference", "finance minister conference with friends", "Jane Doe", "London")
reel1.liked()  # 2
reel2.liked()  # 1
reel1.disliked()  # 1
reel1.display_likes()
reel2.display_likes()
reel1.display_creator_name()
reel1.display_location()
reel1.add_comment("Great dance move!")
reel1.add_comment("Love it!")
reel1.display_comments()
print(id(reel1))
print(id(reel2))
