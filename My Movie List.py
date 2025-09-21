# My movie list

# 1. Create a list of favorite movies (less popular ones)
movies = ["Coherence", "The Man from Earth", "Timecrimes", "Pontypool"]

# Show current movies
print("Your current favorite movies are:")
print(movies)

# 2. Let the user add a new movie
new_movie = input("Enter a movie you want to add: ")
movies.append(new_movie)
print(f"{new_movie} has been added to your list.")

# 3. Let the user remove a movie
remove_movie = input("Enter a movie you want to remove: ")
if remove_movie in movies:
    movies.remove(remove_movie)
    print(f"{remove_movie} has been removed from your list.")
else:
    print(f"{remove_movie} is not in your list.")

# 4. Print the final sorted list
movies.sort()
print("Here is your final list of favorite movies (sorted):")
print(movies)
