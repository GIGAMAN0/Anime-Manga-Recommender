import Project

def test_fetch_anime_details():
    anime_details = Project.fetch_anime_details("Naruto")
    assert anime_details["Eng Title"] == "Naruto"
    assert anime_details["Jap Title"] == "Naruto"
    assert anime_details["Bio"] != ""
    assert anime_details["Rating"] != ""
    assert anime_details["Episode Count"] != ""

def test_suggest_random_anime():
    anime_details = Project.suggest_random_anime()
    assert anime_details != "No anime found."
    assert anime_details != "Error occurred while fetching anime details."

def test_main():
    # Test case for providing anime names
    Project.input = lambda _: "Naruto, One Piece"
    Project.main()

    # Test case for getting a random suggestion
    Project.input = lambda _: ""
    Project.main()