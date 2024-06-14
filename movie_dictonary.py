#saiprasad Pujari
#creating a dictonary that contanins movie name, director and leading actor
def main ():
    movies = {
        "bangaarada manushya": {"actor": "rajkumar", "director": "siddalingaiah"},
        "mayabazar": {"actor": "ntr", "director": "kv reddy"},
        "jailer": {"actor": "rajinikanth", "director": "nelson dilipkumar"},
        "sholay": {"actor": "amitab bacchan", "director": "ramesh sippy"},
        "life of pai": {"actor": "suraj sharma", "director": "ang lee"}
    }  # Create a dictionary of movie names and leading actors
    print("original dictionary of movies :")  # Printing the dictionary of movies
    print(movies)
    # Loop through the dictionary and print movie, actors and director
    print("Movies and their lead actors and directors:")
    for movie, details in movies.items():
        print(f"Movie: {movie}, Actor: {details['actor']}, Director: {details['director']}")
    movies["rrr"] = {"actor": "ram charan", "director": "ss rajamouli"}  # adding new entry
    print("\nUpdated Dictionary after adding 'rrr':")  # reprinting the dictionary
    print(movies)
    # entering movie name to find its star
    movie_search = input("\nEnter a movie name to find its star: ")
    if movie_search in movies:
        print(f"The leading actor in '{movie_search}' is {movies[movie_search]['actor']}")
    else:
        print("Movie not found in the dictionary.")

if __name__ == "__main__":
    main()

