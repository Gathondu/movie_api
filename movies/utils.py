# return the index where the id lies if present, else false
def binarySearch(movies, start, end, id):
    # check base case
    if start <= end:
        mid = int((start + (end))/2)
        if movies[mid]['id'] == id:
            return movies[mid]
        # if movie id is smaller than mid, then it's in the left subarray
        elif movies[mid]['id'] > id:
            return binarySearch(movies, start, mid-1, id)
        # else it can only be in the right subarray
        else:
            return binarySearch(movies, mid+1, end, id)
    else:
        # element is not present
        return False

def linearSearch(movies, key, query):
    results = []
    for movie in movies:
        if query.lower() in movie.get(key, None).lower():
            results.append(movie)
    return results
