import random
from .styles import get_cyberpunk_styles

def generate_activity():
    # Generate 52 weeks * 7 days of rects
    heatmap = ""
    for w in range(52):
        for d in range(7):
            x = 40 + (w * 14)
            y = 100 + (d * 14)
            
            # Randomly highlight some dots for a cyberpunk feel
            val = random.random()
            animate_tag = ""
            if val > 0.95:
                fill = "#00ffcc"
                glow = 'filter="url(#neon-glow)"'
                dur = round(random.uniform(2.0, 4.0), 1)
                animate_tag = f'<animate attributeName="opacity" values="1;0.4;1" dur="{dur}s" repeatCount="indefinite" />'
            elif val > 0.8:
                fill = "#58a6ff"
                glow = ""
                if random.random() > 0.5:
                    dur = round(random.uniform(3.0, 6.0), 1)
                    animate_tag = f'<animate attributeName="opacity" values="1;0.6;1" dur="{dur}s" repeatCount="indefinite" />'
            elif val > 0.6:
                fill = "#21262d"
                glow = ""
            else:
                fill = "#161b22"
                glow = ""
                
            heatmap += f'<rect x="{x}" y="{y}" width="10" height="10" fill="{fill}" stroke="#30363d" stroke-width="1" rx="2" {glow}>{animate_tag}</rect>\n'

    svg = f"""
    <svg width="800" height="240" viewBox="0 0 800 240" fill="none" xmlns="http://www.w3.org/2000/svg">
        {get_cyberpunk_styles()}
        <rect width="800" height="240" class="bg"/>
        
        <!-- Outer Glowing Box -->
        <rect x="20" y="20" width="760" height="200" class="glow-border"/>
        <rect x="21" y="21" width="758" height="198" class="panel"/>
        
        <!-- Header -->
        <text x="40" y="60" class="text-title" font-size="24">Contribution Activity</text>
        <text x="40" y="80" class="text-subtitle" font-size="12">0 contributions in the last year</text>
        
        <g transform="translate(620, 60)">
            <text x="0" y="10" class="text-subtitle" font-size="10">Less</text>
            <rect x="30" y="0" width="10" height="10" fill="#161b22" rx="2"/>
            <rect x="44" y="0" width="10" height="10" fill="#21262d" rx="2"/>
            <rect x="58" y="0" width="10" height="10" fill="#58a6ff" rx="2"/>
            <rect x="72" y="0" width="10" height="10" fill="#00ffcc" rx="2"/>
            <text x="90" y="10" class="text-subtitle" font-size="10">More</text>
        </g>
        
        {heatmap}
        
    </svg>
    """
    return svg
