from .styles import get_cyberpunk_styles

def generate_stack(languages):
    # Take top 3
    top_langs = languages[:3]
    total_count = sum(l[1] for l in languages) if languages else 1
    
    colors = ['#9e60ff', '#ff5a36', '#e3b341']
    
    bars = ""
    for i, (lang, count) in enumerate(top_langs):
        percent = int((count / total_count) * 100)
        color = colors[i % len(colors)]
        
        y_offset = 110 + (i * 35)
        
        bars += f"""
        <circle cx="45" cy="{y_offset - 4}" r="4" fill="{color}"/>
        <text x="65" y="{y_offset}" class="text-main" font-weight="bold">{lang}</text>
        <text x="240" y="{y_offset}" class="text-accent" fill="{color}">{percent}%</text>
        
        <rect x="280" y="{y_offset - 8}" width="450" height="8" class="progress-bg"/>
        <rect x="280" y="{y_offset - 8}" width="{450 * (percent/100)}" height="8" class="progress-fill" fill="{color}"/>
        """

    svg = f"""
    <svg width="800" height="240" viewBox="0 0 800 240" fill="none" xmlns="http://www.w3.org/2000/svg">
        {get_cyberpunk_styles()}
        <rect width="800" height="240" fill="url(#bg-gradient)"/>
        
        <!-- Outer Glowing Box -->
        <rect x="20" y="20" width="760" height="200" class="glow-border"/>
        <rect x="21" y="21" width="758" height="198" class="panel"/>
        
        <!-- Header -->
        <text x="40" y="60" class="text-title" font-size="24">Language Stack</text>
        <text x="40" y="80" class="text-subtitle">Repository-weighted technologies</text>
        
        <text x="750" y="60" text-anchor="end" class="text-accent" fill="#58a6ff">&gt; stack.scan</text>
        
        {bars}
    </svg>
    """
    return svg
