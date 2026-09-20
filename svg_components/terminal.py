from .styles import get_cyberpunk_styles

def generate_terminal(user_data, stats, repos):
    login = user_data.get('login', 'developer')
    followers = user_data.get('followers', 0)
    repos_count = user_data.get('public_repos', 0)
    stars = stats.get('total_stars', 0)
    
    ascii_art = [
        "  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ",
        "  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ",
        "  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ",
        "  . . . . . . . . . . . . . /\\\\ . . . . . . . . . . . . . . . . . . . . . ",
        "  . . . . . . . . . . . . /  \\\\ . . . . . . . . . . . . . . . . . . . . . ",
        "  . . . . . . . . . . . /____\\\\ . . . . . . . . . . . . . . . . . . . . . ",
        "  . . . . . . . . . . . |    | . . . . . . . . . . . . . . . . . . . . . ",
        "  . . . . . . . . . . . |____| . . . . . . . . . . . . . . . . . . . . . ",
        "  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ",
        "  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . "
    ]
    
    y_start = 80
    ascii_text = ""
    for i, line in enumerate(ascii_art):
        ascii_text += f'<text x="40" y="{y_start + i*16}" class="text-mono" fill="#00ff00" opacity="0.6" font-size="10">{line}</text>\n'

    top_languages = ", ".join([l[0] for l in stats.get('languages', [])[:3]]) if stats.get('languages') else "N/A"

    svg = f"""
    <svg width="800" height="400" viewBox="0 0 800 400" fill="none" xmlns="http://www.w3.org/2000/svg">
        {get_cyberpunk_styles()}
        <rect width="800" height="400" fill="url(#bg-gradient)"/>
        
        <!-- Outer Glowing Box -->
        <rect x="20" y="20" width="760" height="360" class="glow-border"/>
        <rect x="21" y="21" width="758" height="358" class="panel"/>
        
        <!-- Terminal Header -->
        <circle cx="40" cy="40" r="4" fill="#ff5f56"/>
        <circle cx="55" cy="40" r="4" fill="#ffbd2e"/>
        <circle cx="70" cy="40" r="4" fill="#27c93f"/>
        
        <text x="400" y="44" text-anchor="middle" class="text-accent" font-size="12">{login}@github ~ $ ./profile-scan --live</text>
        
        <text x="750" y="44" text-anchor="end" class="text-glow" fill="#00ffcc" font-size="12">● LIVE</text>
        
        <line x1="21" y1="55" x2="779" y2="55" stroke="#30363d" stroke-width="1"/>
        
        <!-- Left Panel: Visual Map -->
        <rect x="35" y="70" width="350" height="295" fill="transparent" stroke="#30363d" stroke-width="1" rx="4"/>
        <text x="45" y="85" class="text-accent" font-size="10">VISUAL.MAP</text>
        {ascii_text}
        
        <!-- A glowing horizontal line simulating a scanner -->
        <rect x="35" y="150" width="350" height="2" fill="#00ffcc" filter="url(#neon-glow)"/>
        <rect x="35" y="140" width="350" height="20" fill="#00ffcc" opacity="0.1"/>
        
        <!-- Right Panel: System Info -->
        <rect x="400" y="70" width="365" height="295" fill="transparent" stroke="#30363d" stroke-width="1" rx="4"/>
        <text x="410" y="85" class="text-accent" font-size="10">SYSTEM.INFO</text>
        
        <g transform="translate(410, 110)">
            <text x="0" y="0" class="text-accent">Subject</text>
            <text x="120" y="0" class="text-main">{user_data.get('name', login)}</text>
            <line x1="0" y1="5" x2="340" y2="5" stroke="#30363d" stroke-width="1" stroke-dasharray="2,2"/>
            
            <text x="0" y="25" class="text-accent">Handle</text>
            <text x="120" y="25" class="text-main">@{login}</text>
            <line x1="0" y1="30" x2="340" y2="30" stroke="#30363d" stroke-width="1" stroke-dasharray="2,2"/>
            
            <text x="0" y="50" class="text-accent">Role</text>
            <text x="120" y="50" class="text-main">Developer</text>
            <line x1="0" y1="55" x2="340" y2="55" stroke="#30363d" stroke-width="1" stroke-dasharray="2,2"/>
            
            <!-- Highlighted Status Row -->
            <rect x="-5" y="62" width="350" height="24" fill="#00ffcc" opacity="0.1" rx="4"/>
            <text x="0" y="78" class="text-glow">Status</text>
            <text x="120" y="78" class="text-glow">Building | Learning | Shipping</text>
            <line x1="0" y1="88" x2="340" y2="88" stroke="#30363d" stroke-width="1" stroke-dasharray="2,2"/>
            
            <text x="0" y="110" class="text-accent">Languages</text>
            <text x="120" y="110" class="text-main">{top_languages}</text>
            <line x1="0" y1="115" x2="340" y2="115" stroke="#30363d" stroke-width="1" stroke-dasharray="2,2"/>
            
            <text x="0" y="135" class="text-accent">Repositories</text>
            <text x="120" y="135" class="text-main">{repos_count}</text>
            <line x1="0" y1="140" x2="340" y2="140" stroke="#30363d" stroke-width="1" stroke-dasharray="2,2"/>
            
            <text x="0" y="160" class="text-accent">Stars</text>
            <text x="120" y="160" class="text-main">{stars}</text>
            <line x1="0" y1="165" x2="340" y2="165" stroke="#30363d" stroke-width="1" stroke-dasharray="2,2"/>
            
            <text x="0" y="185" class="text-accent">Followers</text>
            <text x="120" y="185" class="text-main">{followers}</text>
            <line x1="0" y1="190" x2="340" y2="190" stroke="#30363d" stroke-width="1" stroke-dasharray="2,2"/>
            
            <text x="0" y="210" class="text-accent">Contact</text>
            <text x="120" y="210" class="text-main">github.com/{login}</text>
        </g>
    </svg>
    """
    return svg
