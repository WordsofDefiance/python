books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

print("Suggested gift: {}".format(books[0]))

for book in books:
    print("* " + book)

video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Assasin's Creed: Unity"
]

for game in video_games:
    print("* " + game)

def display_wishlist(display_name, wishes):
    items = wishes
    print(display_name + ":")
    suggested_gift = wishes.pop(0)
    print("=============>", suggested_gift, "<=========")
    for wish in items:
        print("* " + wish)
    print()

display_wishlist("Books", books)
display_wishlist("Video Games", video_games)
