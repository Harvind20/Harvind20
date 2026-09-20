import os
import requests
from io import BytesIO
from PIL import Image
import pyfiglet

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = os.getenv("GITHUB_USERNAME", "Harvind20")

headers = {}
if GITHUB_TOKEN:
    headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

def get_user_data():
    if GITHUB_TOKEN:
        response = requests.get("https://api.github.com/user", headers=headers)
        if response.status_code == 200:
            return response.json()
    
    url = f"https://api.github.com/users/{USERNAME}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return {"login": USERNAME, "avatar_url": ""}

def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=100"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return []

def calculate_stats(repos):
    languages = {}
    for repo in repos:
        lang = repo.get('language')
        if lang:
            languages[lang] = languages.get(lang, 0) + 1
            
    sorted_langs = sorted(languages.items(), key=lambda item: item[1], reverse=True)
    return {"languages": sorted_langs}

def generate_ascii_avatar(url, width=70):
    if not url: return []
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        aspect_ratio = img.height / img.width
        # terminal characters are about twice as tall as they are wide
        new_height = int(aspect_ratio * width * 0.5)
        img = img.resize((width, new_height))
        img = img.convert('RGB')
        
        chars = ["@", "%", "#", "*", "+", "=", "-", ":", ".", " "]
        ascii_pixels = []
        for y in range(new_height):
            row = []
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                gray = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
                char = chars[gray * len(chars) // 256]
                row.append((char, f"#{r:02x}{g:02x}{b:02x}"))
            ascii_pixels.append(row)
        return ascii_pixels
    except Exception as e:
        print(f"Error generating avatar: {e}")
        return []

def generate_banner(username, ascii_pixels):
    # Generate figlet text
    figlet_text = pyfiglet.figlet_format(username.upper(), font="standard").split('\n')
    
    # Render figlet text (Above)
    text_svg = ""
    start_y = 60
    for i, line in enumerate(figlet_text):
        if not line.strip(): continue
        y_pos = start_y + (i * 16)
        clean_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        # Blue/cyan theme
        text_svg += f'<text x="40" y="{y_pos}" font-family="monospace" font-size="14" fill="#00ccff" xml:space="preserve">{clean_line}</text>\\n'

    # Avatar (BIG below)
    avatar_svg = ""
    avatar_start_y = start_y + (len(figlet_text) * 16) + 20
    for i, row in enumerate(ascii_pixels):
        y_pos = avatar_start_y + (i * 10)
        row_content = "".join([f'<tspan fill="{color}">{char}</tspan>' for char, color in row])
        avatar_svg += f'<text x="40" y="{y_pos}" font-family="monospace" font-size="10" xml:space="preserve">{row_content}</text>\\n'
    
    height = avatar_start_y + (len(ascii_pixels) * 10) + 40
    
    svg = f"""
    <svg width="800" height="{height}" viewBox="0 0 800 {height}" xmlns="http://www.w3.org/2000/svg">
        <style>
            .bg {{ fill: #0d1117; }}
            text {{ font-family: ui-monospace, SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace; }}
            .border {{ fill: none; stroke: #00ff00; stroke-width: 2px; stroke-dasharray: 10 5; rx: 8px; }}
        </style>
        <rect width="800" height="{height}" class="bg"/>
        <!-- Green box container -->
        <rect x="20" y="20" width="760" height="{height - 40}" class="border"/>
        {text_svg}
        {avatar_svg}
    </svg>
    """
    return svg

def generate_stack(languages):
    svg_content = ""
    total = sum(count for _, count in languages)
    
    y_start = 50
    svg_content += f'<text x="20" y="30" font-size="16" fill="#00ccff" font-weight="bold" xml:space="preserve">=== Tech Stack ===</text>\\n'
    
    for i, (lang, count) in enumerate(languages):
        percent = (count / total) * 100
        bar_len = int(percent / 2) # max 50 chars
        bar_filled = "█" * bar_len
        bar_empty = " " * (50 - bar_len)
        
        colors = ["#00ccff", "#0099cc", "#006699", "#33ccff", "#66d9ff"]
        color = colors[i % len(colors)]
        
        y_pos = y_start + (i * 20)
        svg_content += f'<text x="20" y="{y_pos}" font-size="14" fill="#c9d1d9" xml:space="preserve">{lang.ljust(12)} [<tspan fill="{color}">{bar_filled}</tspan>{bar_empty}]</text>\\n'

    height = max(100, y_start + (len(languages) * 20) + 20)
    
    svg = f"""
    <svg width="800" height="{height}" viewBox="0 0 800 {height}" xmlns="http://www.w3.org/2000/svg">
        <style>
            .bg {{ fill: #0d1117; }}
            text {{ font-family: ui-monospace, SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace; }}
        </style>
        <rect width="800" height="{height}" class="bg"/>
        {svg_content}
    </svg>
    """
    return svg

def main():
    print("Fetching user data...")
    user_data = get_user_data()
    username = user_data.get('login', USERNAME)
    print(f"Authenticated as {username}")
    
    repos = get_repos(username)
    stats = calculate_stats(repos)
    
    os.makedirs("output", exist_ok=True)
    
    print("Generating ASCII Avatar...")
    ascii_pixels = generate_ascii_avatar(user_data.get('avatar_url'))
    
    with open("output/banner.svg", "w", encoding="utf-8") as f:
        f.write(generate_banner(username, ascii_pixels))
        
    with open("output/stack.svg", "w", encoding="utf-8") as f:
        f.write(generate_stack(stats['languages']))

    print("Generation complete! Check the output/ folder.")

if __name__ == "__main__":
    main()
