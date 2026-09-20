import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = os.getenv("GITHUB_USERNAME", "octocat")

headers = {}
if GITHUB_TOKEN:
    headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

def get_user_data(username):
    # Fetch user data
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching user: {response.status_code}")
        return {"name": username, "login": username, "bio": "Building with CSS on GitHub", "public_repos": 6, "followers": 24000, "avatar_url": ""}

def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=100"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def calculate_stats(repos):
    total_stars = sum(repo.get('stargazers_count', 0) for repo in repos)
    
    # Calculate languages
    languages = {}
    for repo in repos:
        lang = repo.get('language')
        if lang:
            languages[lang] = languages.get(lang, 0) + 1
            
    # Sort languages
    sorted_langs = sorted(languages.items(), key=lambda item: item[1], reverse=True)
    
    return {
        "total_stars": total_stars,
        "languages": sorted_langs
    }

from svg_components.header import generate_header
from svg_components.terminal import generate_terminal
from svg_components.projects import generate_projects
from svg_components.stack import generate_stack
from svg_components.activity import generate_activity

def main():
    print(f"Fetching data for {USERNAME}...")
    user_data = get_user_data(USERNAME)
    repos = get_repos(USERNAME)
    stats = calculate_stats(repos)
    
    # Pass 1: generate all SVGs
    print("Generating SVGs...")
    os.makedirs("output", exist_ok=True)
    
    with open("output/header.svg", "w", encoding="utf-8") as f:
        f.write(generate_header(user_data, stats))
        
    with open("output/terminal.svg", "w", encoding="utf-8") as f:
        f.write(generate_terminal(user_data, stats, repos))
        
    with open("output/projects.svg", "w", encoding="utf-8") as f:
        f.write(generate_projects(repos[:2]))
        
    with open("output/stack.svg", "w", encoding="utf-8") as f:
        f.write(generate_stack(stats['languages']))
        
    with open("output/activity.svg", "w", encoding="utf-8") as f:
        f.write(generate_activity())

    print("Generation complete! Check the output/ folder.")

if __name__ == "__main__":
    main()
