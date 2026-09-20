from .styles import get_cyberpunk_styles

def generate_projects(repos):
    # Take up to 2 repos
    repos = repos[:2]
    
    project_cards = ""
    for i, repo in enumerate(repos):
        name = repo.get('name', 'repo')
        desc = repo.get('description', 'A cool project.') or 'A cool project.'
        # Truncate description
        if len(desc) > 60:
            desc = desc[:57] + '...'
            
        stars = repo.get('stargazers_count', 0)
        language = repo.get('language', 'Unknown')
        
        x_offset = 35 + (i * 365)
        
        project_cards += f"""
        <g transform="translate({x_offset}, 70)">
            <rect x="0" y="0" width="350" height="130" fill="#161b22" stroke="#30363d" stroke-width="1" rx="4"/>
            <rect x="0" y="0" width="350" height="30" fill="#21262d" rx="4"/>
            
            <circle cx="15" cy="15" r="4" fill="#58a6ff"/>
            <text x="30" y="19" class="text-accent" font-size="12">{name}</text>
            
            <text x="15" y="55" class="text-title" font-size="18">{name}</text>
            <text x="15" y="75" class="text-subtitle">{desc}</text>
            
            <!-- Language Pill -->
            <rect x="15" y="95" width="80" height="20" class="tag-pill" rx="10"/>
            <text x="55" y="109" text-anchor="middle" class="tag-text" font-size="10">{language}</text>
            
            <text x="110" y="109" class="text-subtitle" font-size="10">★ {stars}  updated just now</text>
            
            <!-- A decorative circular progress or icon on the right -->
            <circle cx="300" cy="80" r="20" fill="transparent" stroke="#30363d" stroke-width="4"/>
            <circle cx="300" cy="80" r="20" fill="transparent" stroke="#58a6ff" stroke-width="4" stroke-dasharray="80" stroke-dashoffset="20"/>
            <text x="300" y="84" text-anchor="middle" class="text-main" font-size="10" font-weight="bold">88%</text>
        </g>
        """

    svg = f"""
    <svg width="800" height="240" viewBox="0 0 800 240" fill="none" xmlns="http://www.w3.org/2000/svg">
        {get_cyberpunk_styles()}
        <rect width="800" height="240" fill="url(#bg-gradient)"/>
        
        <!-- Outer Glowing Box -->
        <rect x="20" y="20" width="760" height="200" class="glow-border"/>
        <rect x="21" y="21" width="758" height="198" class="panel"/>
        
        <!-- Header -->
        <text x="40" y="50" class="text-title" font-size="14" fill="#58a6ff" letter-spacing="2">PROJECTS.LIST</text>
        <text x="180" y="50" class="text-subtitle">./projects.sh --all</text>
        
        <text x="750" y="50" text-anchor="end" class="text-subtitle">{len(repos)} pinned</text>
        
        <line x1="21" y1="60" x2="779" y2="60" stroke="#30363d" stroke-width="1"/>
        
        {project_cards}
    </svg>
    """
    return svg
