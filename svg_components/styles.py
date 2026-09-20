def get_cyberpunk_styles():
    return """
    <style>
        .bg { fill: #0d1117; }
        .panel { fill: #161b22; stroke: #30363d; stroke-width: 1px; rx: 8px; }
        .glow-border { 
            fill: none; 
            stroke: url(#cyan-glow); 
            stroke-width: 1.5px; 
            rx: 8px; 
        }
        text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; fill: #c9d1d9; }
        .text-title { fill: #ffffff; font-weight: 600; }
        .text-subtitle { fill: #8b949e; }
        .text-accent { fill: #58a6ff; font-family: ui-monospace, SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace; }
        .text-mono { fill: #3fb950; font-family: ui-monospace, SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace; }
        .text-glow { fill: #00ffcc; font-weight: 600; }
        
        .tag-pill { fill: transparent; stroke: #30363d; stroke-width: 1px; rx: 12px; }
        .tag-text { fill: #c9d1d9; font-weight: 600; }
        
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
        <filter id="neon-glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="4" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
    </defs>
    """
