import requests
import random

def fetch_anime_details(anime_name):
    url = f"https://kitsu.io/api/edge/anime?filter[text]={anime_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['data']:
            anime = data['data'][0]
            attributes = anime['attributes']
            titles = attributes['titles']
            english_title = titles.get('en', 'N/A')
            romanized_japanese_title = titles.get('en_jp', 'N/A')
            synopsis = attributes['synopsis']
            rating = attributes['averageRating']
            episode_count = attributes['episodeCount']
            
            # Return the details
            return {
                "Eng Title": english_title,
                "Jap Title": romanized_japanese_title,
                "Bio": synopsis,
                "Rating": rating,
                "Episode Count": episode_count
            }
        else:
            return "Anime not found."
    else:
        return "Error occurred while fetching anime details."

def suggest_random_anime():
    url = "https://kitsu.io/api/edge/anime?page[limit]=1&page[offset]=" + str(random.randint(0, 20000))
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['data']:
            anime_name = data['data'][0]['attributes']['titles']['en_jp']
            return fetch_anime_details(anime_name)
        else:
            return "No anime found."
    else:
        return "Error occurred while fetching anime details."

def main():
    # Prompt the user for anime names
    anime_names = input("Enter Anime Titles To Watch (separated by commas), Or Press Enter To Get a Random Suggestion: ").split(",")

    if anime_names[0] != '':
        # Randomly select an anime from the list
        random_anime = random.choice(anime_names)
        random_anime = random_anime.strip()
        # Capitalize the first letter of the anime name
        random_anime = random_anime.capitalize()
        anime_details = fetch_anime_details(random_anime)
        print("Anime Details:")
        for key, value in anime_details.items():
            print(f"{key}: {value}")
    else:
        anime_details = suggest_random_anime()
        print("Anime Details:")
        for key, value in anime_details.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
