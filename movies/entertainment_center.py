import media
import fresh_tomatoes

toy_story = media.Movie("Toy story", "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "http://www.movieposter.com/posters/archive/main/98/MPW-49246",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

print media.Movie.VALID_RATINGS
print media.Movie.__doc__

movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
