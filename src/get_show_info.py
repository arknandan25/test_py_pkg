import sys
import requests
import subprocess
from typing import List
from src import JINJA_ENVIRONMENT, PWD, URL, WARNING


def get_genre(genre_list: List = None) -> str:
    """Get movie genre information"""
    genre = ", ".join(g for g in genre_list) if genre_list else "Unknown Genre"
    return genre


def get_summary_formatted(summary_str: str) -> str:
    """Get movie summary formatted"""
    return summary_str.replace("<p>", "").replace("</p>", "").replace("<b>", "").replace("</b>", "")


def show_information(args) -> None:
    """Render a web page with movie/show information

    :param args: Namespace
    :return: None
    """
    response = requests.get(URL.format(user_input=args.name))

    if response.status_code != 200 or not response.json():
        print(WARNING + "Looks like something went wrong while getting data from API!! Try again.")
        sys.exit(0)

    top_movie_data = response.json()[0]
    template = JINJA_ENVIRONMENT.get_template(f"web_template.html")
    rendered_html = template.render(
            name=top_movie_data['show']['name'],
            genre=get_genre(top_movie_data['show'].get('genres')),
            premiered=top_movie_data['show'].get('genre', 'Unknown'),
            officialSite=top_movie_data['show'].get('officialSite', 'Unknown'),
            rating=top_movie_data['show']['rating'].get('average', 'Unknown'),
            summary=get_summary_formatted(top_movie_data['show'].get('summary', 'Unknown')),
            img_src=top_movie_data['show']['image']['medium'],
        )
    with open(f'{PWD}/templates/rendered.html', 'w') as f:
        f.write(rendered_html)
    subprocess.call(['open', f'{PWD}/templates/rendered.html'])
