def get_cyberpunk_styles():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&amp;family=Inter:wght@400;600;800&amp;display=swap');
        
        .bg { fill: #0d1117; }
        .panel { fill: #161b22; stroke: #30363d; stroke-width: 1px; rx: 8px; }
        .glow-border { 
            fill: none; 
            stroke: url(#cyan-glow); 
            stroke-width: 1.5px; 
            rx: 8px; 
        }
        .text-main { fill: #c9d1d9; font-family: 'Inter', sans-serif; font-size: 14px; }
        .text-title { fill: #ffffff; font-family: 'Inter', sans-serif; font-weight: 800; font-size: 28px; }
        .text-subtitle { fill: #8b949e; font-family: 'Inter', sans-serif; font-size: 12px; }
        .text-accent { fill: #58a6ff; font-family: 'Fira Code', monospace; font-size: 13px; }
        .text-mono { fill: #3fb950; font-family: 'Fira Code', monospace; font-size: 12px; }
        .text-glow { fill: #00ffcc; font-family: 'Inter', sans-serif; font-weight: 800; }
        
        .tag-pill { fill: transparent; stroke: #30363d; stroke-width: 1px; rx: 12px; }
        .tag-text { fill: #c9d1d9; font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 600; }
        
        .progress-bg { fill: #21262d; rx: 4px; }
        .progress-fill { rx: 4px; }
        
        .dot { fill: #30363d; }
        .dot-glow { fill: #00ffcc; filter: drop-shadow(0 0 5px #00ffcc); }
    </style>
    <defs>
        <linearGradient id="cyan-glow" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#00ffcc" stop-opacity="0.8"/>
            <stop offset="50%" stop-color="#00ffcc" stop-opacity="0.1"/>
            <stop offset="100%" stop-color="#00ffcc" stop-opacity="0.8"/>
        </linearGradient>
        <linearGradient id="bg-gradient" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#0d1117" />
            <stop offset="100%" stop-color="#000000" />
        </linearGradient>
        <filter id="neon-glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="4" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
    </defs>
    """
