import fresh_tomatoes
import media

the_departed = media.Movie("The Departed",
						   "An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.",
						   "http://ia.media-imdb.com/images/M/MV5BMTI1MTY2OTIxNV5BMl5BanBnXkFtZTYwNjQ4NjY3._V1_UX182_CR0,0,182,268_AL_.jpg",
						   "https://www.youtube.com/watch?v=iojhqm0JTW4")

threehundred = media.Movie("300",
						   "King Leonidas of Sparta and a force of 300 men fight the Persians at Thermopylae in 480 B.C.",
						   "http://ia.media-imdb.com/images/M/MV5BMjAzNTkzNjcxNl5BMl5BanBnXkFtZTYwNDA4NjE3._V1_UX182_CR0,0,182,268_AL_.jpg",
						   "https://www.youtube.com/watch?v=UrIbxk7idYA")

interstellar = media.Movie("Interstellar",
						   "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
						   "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UX182_CR0,0,182,268_AL_.jpg",
						   "https://www.youtube.com/watch?v=Lm8p5rlrSkY")

pulp_fiction = media.Movie("Pulp Fiction",
						   "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
						   "http://ia.media-imdb.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_UX182_CR0,0,182,268_AL_.jpg",
						   "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

the_dark_knight = media.Movie("The Dark Knight",
						   "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.",
						   "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
						   "https://www.youtube.com/watch?v=yrJL5JxEYIw")

deadpool = media.Movie("Deadpool",
						   "A former Special Forces operative turned mercenary is subjected to a rogue experiment that leaves him with accelerated healing powers, adopting the alter ego Deadpool.",
						   "http://ia.media-imdb.com/images/M/MV5BMjQyODg5Njc4N15BMl5BanBnXkFtZTgwMzExMjE3NzE@._V1_UY268_CR1,0,182,268_AL_.jpg",
						   "https://www.youtube.com/watch?v=FyKWUTwSYAs&oref=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DFyKWUTwSYAs&has_verified=1")

movies = [the_departed, threehundred, interstellar, pulp_fiction, the_dark_knight, deadpool]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
