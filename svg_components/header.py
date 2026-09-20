from .styles import get_cyberpunk_styles

def generate_header(user_data, stats):
    name = user_data.get('name', 'Developer')
    login = user_data.get('login', 'developer')
    bio = user_data.get('bio', 'Building cool things on GitHub.') or 'Building cool things on GitHub.'
    stars = stats.get('total_stars', 0)
    
    # We will just draw a cyberpunk header box
    svg = f"""
    <svg width="800" height="200" viewBox="0 0 800 200" fill="none" xmlns="http://www.w3.org/2000/svg">
        {get_cyberpunk_styles()}
        <rect width="800" height="200" fill="url(#bg-gradient)"/>
        
        <!-- Outer Glowing Box -->
        <rect x="20" y="20" width="760" height="160" class="glow-border"/>
        
        <!-- Inner Box -->
        <rect x="21" y="21" width="758" height="158" class="panel"/>
        
        <!-- Avatar Placeholder (using a simple circle if we can't embed the actual image easily in static SVG without base64) -->
        <circle cx="100" cy="100" r="45" fill="#21262d" stroke="#58a6ff" stroke-width="2"/>
        <text x="100" y="105" text-anchor="middle" class="text-accent" font-size="24">{'@'+login[0].upper()}</text>
        
        <!-- Handle & Name -->
        <text x="170" y="65" class="text-accent">@{login}</text>
        <text x="170" y="100" class="text-title">{name}</text>
        <text x="170" y="125" class="text-subtitle">{bio}</text>
        
        <!-- Tags -->
        <g transform="translate(170, 145)">
            <rect x="0" y="0" width="80" height="24" class="tag-pill"/>
            <text x="40" y="16" text-anchor="middle" class="tag-text">Developer</text>
            
            <rect x="90" y="0" width="80" height="24" class="tag-pill"/>
            <text x="130" y="16" text-anchor="middle" class="tag-text">Open Source</text>
        </g>
        
        <!-- Total Stars -->
        <g transform="translate(650, 100)">
            <text x="50" y="-10" text-anchor="middle" class="text-title" fill="#58a6ff" font-size="32">{stars}</text>
            <text x="50" y="15" text-anchor="middle" class="text-subtitle" font-weight="600" letter-spacing="2">TOTAL STARS</text>
        </g>
    </svg>
    """
    return svg
