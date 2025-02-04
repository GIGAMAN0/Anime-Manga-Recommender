import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import requests
import random

# Replace with your actual Client ID obtained from MyAnimeList
CLIENT_ID = ''

def get_anime_details(anime_name: str) -> dict:
    endpoint = 'https://api.myanimelist.net/v2/anime'
    params = {
        'q': anime_name,
        'limit': 1
    }

    headers = {
        'X-MAL-CLIENT-ID': CLIENT_ID
    }

    response = requests.get(endpoint, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data.get('data') and len(data['data']) > 0:
            return data['data'][0]

    return None

def get_manga_details(manga_name: str) -> dict:
    endpoint = 'https://api.myanimelist.net/v2/manga'
    params = {
        'q': manga_name,
        'limit': 1
    }

    headers = {
        'X-MAL-CLIENT-ID': CLIENT_ID
    }

    response = requests.get(endpoint, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data.get('data') and len(data['data']) > 0:
            return data['data'][0]

    return None

def validate_anime(anime_name: str) -> bool:
    anime_details = get_anime_details(anime_name)
    return anime_details is not None

def suggest_correct_name(item_name: str, endpoint: str) -> None:
    suggestion_endpoint = f"{endpoint}?q={item_name}"
    response = requests.get(suggestion_endpoint)

    if response.status_code == 200:
        data = response.json()
        if data.get('data') and len(data['data']) > 0:
            suggestions = [item['node']['title'] for item in data['data'] if item['node'].get('title_english')]
            print("Did you mean one of the following?")
            for suggestion in suggestions:
                print("-", suggestion)
    else:
        print("Failed to fetch suggestions. Please try again later.")


def validate_manga(manga_name: str) -> bool:
    manga_details = get_manga_details(manga_name)
    return manga_details is not None

def create_feature_vector(title: str, keywords: list) -> list:
    feature_vector = [1 if keyword in title.lower() else 0 for keyword in keywords]
    return feature_vector

def create_user_profile(watched_items: tuple, selected_genres: list) -> pd.DataFrame:
    user_profile = {'title': [], 'genre': []}

    # Add watched items and selected genres to the user profile
    for item in watched_items:
        user_profile['title'].append(item)
        user_profile['genre'].append('Watched')

    for genre in selected_genres:
        user_profile['title'].append('Selected Genre')
        user_profile['genre'].append(genre)

    return pd.DataFrame(user_profile)


def prepare_data(watched_items: tuple, selected_genres: list) -> pd.DataFrame:
    # Create an empty list to store data
    anime_manga_data = []

    # Fetch anime and manga details for watched items
    for item in watched_items:
        if validate_anime(item):
            anime_details = get_anime_details(item)
            genres = anime_details['node']['genres'] if 'genres' in anime_details['node'] else []
            anime_manga_data.append({'Title': anime_details['node']['title'], 'Type': 'Anime', 'Genre': genres})
        elif validate_manga(item):
            manga_details = get_manga_details(item)
            genres = manga_details['node']['genres'] if 'genres' in manga_details['node'] else []
            anime_manga_data.append({'Title': manga_details['node']['title'], 'Type': 'Manga', 'Genre': genres})

    # Add selected genres to the list
    for genre in selected_genres:
        anime_manga_data.append({'Title': 'Selected Genre', 'Type': 'Genre', 'Genre': [genre]})

    # Create DataFrame and return a copy
    return pd.DataFrame(anime_manga_data).copy()

def get_recommendation(item_type: str, watched_items: tuple, selected_genres: list) -> str:
    # Prepare data
    anime_manga_data = prepare_data(watched_items, selected_genres)

    # Filter data based on item type (anime/manga)
    filtered_data = anime_manga_data[anime_manga_data['Type'] == item_type.capitalize()].copy()  # Add .copy()

    # Generate TF-IDF vectors for the titles
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(filtered_data['Title'])

    # Calculate cosine similarity between user profile and anime/manga titles
    user_profile = create_user_profile(watched_items, selected_genres)
    user_tfidf = tfidf_vectorizer.transform(user_profile['title'])
    cosine_sim = cosine_similarity(user_tfidf, tfidf_matrix)

    # Get indices of titles sorted by similarity score
    sim_scores = list(enumerate(cosine_sim[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Find titles not in watched items
    recommended_titles = []
    for idx, score in sim_scores:
        if filtered_data.iloc[idx]['Title'] not in watched_items:
            recommended_titles.append(filtered_data.iloc[idx]['Title'])

    # Remove input title from the recommendation list if present
    if recommended_titles and recommended_titles[0] == watched_items[0]:
        recommended_titles.pop(0)

    # Randomly select a recommendation from the list
    if recommended_titles:
        return random.choice(recommended_titles)
    else:
        return None


def get_user_input() -> tuple:
    watched_anime = []
    watched_manga = []

    while True:
        anime_name = input("Enter the name of an anime you have watched and finished (or 'done' to finish): ").strip()
        if anime_name.lower() == 'done':
            break

        if validate_anime(anime_name):
            watched_anime.append(anime_name)
        else:
            print("Anime not found. Please enter a valid anime name.")
            suggest_correct_name(anime_name, 'https://api.myanimelist.net/v2/anime')

    while True:
        manga_name = input("Enter the name of a manga you have read and finished (or 'done' to finish): ").strip()
        if manga_name.lower() == 'done':
            break

        if validate_manga(manga_name):
            watched_manga.append(manga_name)
        else:
            print("Manga not found. Please enter a valid manga name.")
            suggest_correct_name(manga_name, 'https://api.myanimelist.net/v2/manga')

    return tuple(watched_anime), tuple(watched_manga)

def select_genres() -> list:
    # List of genres
    genres = [
        # Genres
        "Action", "Adventure", "Avant Garde", "Award Winning", "Boys Love",
        "Comedy", "Drama", "Fantasy", "Girls Love", "Gourmet", "Horror", "Mystery",
        "Romance", "Sci-Fi", "Slice of Life", "Sports", "Supernatural", "Suspense",
        # Explicit Genres
        "Ecchi", "Erotica", "Hentai",
        # Themes
        "Adult Cast", "Anthropomorphic", "CGDCT", "Childcare", "Combat Sports",
        "Crossdressing", "Delinquents", "Detective", "Educational", "Gag Humor", "Gore",
        "Harem", "High Stakes Game", "Historical", "Idols (Female)", "Idols (Male)",
        "Isekai", "Iyashikei", "Love Polygon", "Magical Sex Shift", "Mahou Shoujo",
        "Martial Arts", "Mecha", "Medical", "Military", "Music", "Mythology",
        "Organized Crime", "Otaku Culture", "Parody", "Performing Arts", "Pets",
        "Psychological", "Racing", "Reincarnation", "Reverse Harem", "Romantic Subtext",
        "Samurai", "School", "Showbiz", "Space", "Strategy Game", "Super Power",
        "Survival", "Team Sports", "Time Travel", "Vampire", "Video Game",
        "Visual Arts", "Workplace",
        # Demographics
        "Josei", "Seinen", "Shoujo", "Shounen"
    ]

    print("Select Genres:")
    for i, genre in enumerate(genres, 1):
        print(f"{i}: {genre}")

    selected_genres = []
    while True:
        genre_input = input("Enter the number corresponding to your fav genre (or 'done' to finish): ").strip()
        if genre_input.lower() == 'done':
            break

        # Validate genre input
        try:
            genre_number = int(genre_input)
            if genre_number < 1 or genre_number > len(genres):
                print("Invalid genre number. Please enter a valid number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Add selected genre to the list
        selected_genre = genres[genre_number - 1]  # Adjust index since numbering starts from 1
        selected_genres.append(selected_genre)

    return selected_genres

def select_item_type() -> str:
    while True:
        item_type = input("Enter the type of item you want recommendation for (anime/manga): ").strip().lower()
        if item_type not in ['anime', 'manga']:
            print("Invalid item type. Please select 'anime' or 'manga'.")
            continue
        else:
            return item_type

def suggest_recommendation(watched_items: tuple, selected_genres: list) -> str:
    while True:
        item_type = select_item_type()
        recommendation = get_recommendation(item_type, watched_items, selected_genres)
        if recommendation:
            print("Recommended Title:", recommendation)
            return recommendation
        else:
            print("Sorry, there are no recommendations available based on your preferences.")

if __name__ == '__main__':
    watched_anime, watched_manga = get_user_input()
    selected_genres = select_genres()

    recommendation = suggest_recommendation(watched_anime, selected_genres)
    print("Final Recommendation:", recommendation)
