# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# 1. Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def is_good_enough(movie_name):
  for movie_info in movies:
    if movie_info["name"] == movie_name:
      return movie_info["imdb"] > 5.5
  
  return False # in case we couldn't find the movie in the list

# 2. Write a function that returns a sublist of movies with an IMDB score above 5.5.
def filter_movies():
  return list(filter(lambda movie_info : movie_info["imdb"] > 5.5, movies))

# 3. Write a function that takes a category name and returns just those movies under that category.
def filter_category(category):
  return list(filter(lambda movie_info : movie_info["category"] == category, movies))

# 4. Write a function that takes a list of movies and computes the average IMDB score.
def average_score(movies):
  total_imdb = 0
  for movie_info in movies:
    total_imdb += movie_info["imdb"]
  
  return total_imdb / len(movies) if len(movies) != 0 else 0 # in case we don't have any movie in the list

# 5. Write a function that takes a category and computes the average IMDB score.
def average_category_score(category):
  filtered_movies = filter_category(category)
  return average_score(filtered_movies)