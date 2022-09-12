import requests


ALL_SUPERHEROES_URL = "https://akabab.github.io/superhero-api/api/all.json"
SUPERHEROES_FOR_COMPARE = ["Hulk", "Captain America", "Thanos"]


def get_all_superheroes_info(url):
    all_superheroes_response = requests.get(url)

    if not all_superheroes_response.ok:
        return None

    all_superheroes_info = all_superheroes_response.json()

    return all_superheroes_info


def find_smartest_superhero(superheroes_list, all_superheroes_info):
    smartest_superhero = None
    smartest_superhero_intelligence = None

    for superhero in all_superheroes_info:
        if superhero["name"] in superheroes_list:
            superhero_intelligence = superhero["powerstats"]["intelligence"]
            if not smartest_superhero_intelligence or \
                    superhero_intelligence > smartest_superhero_intelligence:
                smartest_superhero = superhero["name"]
                smartest_superhero_intelligence = superhero_intelligence
                continue
            if superhero_intelligence == smartest_superhero_intelligence:
                smartest_superhero += ", " + superhero["name"]

    return smartest_superhero


def main():
    all_superheroes_info = get_all_superheroes_info(ALL_SUPERHEROES_URL)
    smartest_superhero = find_smartest_superhero(SUPERHEROES_FOR_COMPARE, all_superheroes_info)
    print(f"Самый умный супергерой (супергерои) — {smartest_superhero}")


if __name__ == "__main__":
    main()
