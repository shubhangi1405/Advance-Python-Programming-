class Movie:
    def __init__(self, movie_name, rating, ticket_price):
        self.movie_name = movie_name
        self.rating = rating
        self.ticket_price = ticket_price

    def categorize(self):
        if self.rating >= 8:
            return "Hit"
        elif self.rating >= 5:
            return "Average"
        else:
            return "Flop"


class Cinema:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        print("\n--- Movie Collection ---")
        for movie in self.movies:
            print("Movie Name:", movie.movie_name)
            print("Rating:", movie.rating)
            print("Ticket Price:", movie.ticket_price)
            print("Category:", movie.categorize())
            print()


# Creating Cinema object
cinema = Cinema()

# Adding movies
m1 = Movie("3 Idiots", 9.0, 200)
m2 = Movie("Movie B", 6.5, 180)
m3 = Movie("Movie C", 4.0, 150)

cinema.add_movie(m1)
cinema.add_movie(m2)
cinema.add_movie(m3)

# Display movie details
cinema.display_movies()
