#!/usr/bin/env python3
"""
Create a simple HTML presentation from the notebook JSON.
This creates a browser-viewable version without requiring nbconvert.
"""

import json
import html
from pathlib import Path

def escape_html(text):
    """Escape HTML special characters."""
    return html.escape(text)

def markdown_to_html(markdown_text):
    """Simple markdown to HTML converter for basic formatting."""
    lines = markdown_text.split('\n')
    html_lines = []
    in_list = False
    
    for line in lines:
        line = line.strip()
        if not line:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append('<br>')
            continue
            
        # Headers
        if line.startswith('# '):
            html_lines.append(f'<h1>{escape_html(line[2:])}</h1>')
        elif line.startswith('## '):
            html_lines.append(f'<h2>{escape_html(line[3:])}</h2>')
        elif line.startswith('### '):
            html_lines.append(f'<h3>{escape_html(line[4:])}</h3>')
        # Bold
        elif '**' in line:
            parts = line.split('**')
            result = []
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    result.append(escape_html(part))
                else:
                    result.append(f'<strong>{escape_html(part)}</strong>')
            html_lines.append(f'<p>{"".join(result)}</p>')
        # Lists
        elif line.startswith('- ') or line.startswith('* '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            content = escape_html(line[2:])
            html_lines.append(f'<li>{content}</li>')
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(f'<p>{escape_html(line)}</p>')
    
    if in_list:
        html_lines.append('</ul>')
    
    return '\n'.join(html_lines)

def create_html_presentation():
    """Create HTML presentation from notebook."""
    
    notebook_path = Path("notebooks/aavail_presentation.ipynb")
    output_path = Path("reports/aavail_presentation.html")
    assets_dir = Path("reports/assets")
    
    if not notebook_path.exists():
        print(f"Error: Notebook not found at {notebook_path}")
        return False
    
    print(f"Reading notebook: {notebook_path}")
    
    # Read notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Build HTML
    html_parts = []
    html_parts.append("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AAVAIL Market Analysis Presentation</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: #1a1a1a;
            color: #e0e0e0;
            line-height: 1.6;
        }
        .slide {
            min-height: 100vh;
            padding: 60px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            page-break-after: always;
        }
        .slide h1 {
            font-size: 3em;
            margin-bottom: 20px;
            color: #60a5fa;
        }
        .slide h2 {
            font-size: 2.5em;
            margin-bottom: 30px;
            color: #93c5fd;
            border-bottom: 3px solid #3b82f6;
            padding-bottom: 15px;
            width: 100%;
        }
        .slide h3 {
            font-size: 1.8em;
            margin: 20px 0;
            color: #a5b4fc;
        }
        .slide p {
            font-size: 1.3em;
            margin: 15px 0;
            max-width: 900px;
        }
        .slide ul, .slide ol {
            text-align: left;
            max-width: 800px;
            font-size: 1.2em;
            margin: 20px auto;
        }
        .slide li {
            margin: 10px 0;
        }
        .slide strong {
            color: #60a5fa;
        }
        .slide code {
            background: #2d2d2d;
            padding: 2px 8px;
            border-radius: 4px;
            font-family: 'Monaco', monospace;
            color: #fbbf24;
        }
        .slide pre {
            background: #2d2d2d;
            padding: 20px;
            border-radius: 8px;
            text-align: left;
            max-width: 900px;
            overflow-x: auto;
            margin: 20px 0;
        }
        .content {
            max-width: 1000px;
            width: 100%;
        }
        .navigation {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: rgba(0,0,0,0.7);
            padding: 15px;
            border-radius: 8px;
            z-index: 1000;
        }
        .navigation button {
            background: #3b82f6;
            color: white;
            border: none;
            padding: 10px 20px;
            margin: 0 5px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
        }
        .navigation button:hover {
            background: #2563eb;
        }
        img {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            margin: 20px 0;
        }
        @media print {
            .navigation { display: none; }
            .slide { page-break-after: always; }
        }
    </style>
</head>
<body>
    <div class="navigation">
        <button onclick="previousSlide()">← Previous</button>
        <button onclick="nextSlide()">Next →</button>
        <span id="slideNum" style="color: white; margin: 0 10px;">1 / 1</span>
    </div>
""")
    
    # Process cells
    slide_num = 0
    current_slide = []
    
    for cell in nb['cells']:
        slide_type = cell.get('metadata', {}).get('slideshow', {}).get('slide_type', 'skip')
        
        if slide_type == 'skip':
            continue
        
        if slide_type == 'slide' and current_slide:
            # Close previous slide
            html_parts.append('<div class="slide">')
            html_parts.append('<div class="content">')
            html_parts.extend(current_slide)
            html_parts.append('</div></div>')
            current_slide = []
            slide_num += 1
        
        if cell['cell_type'] == 'markdown':
            source = ''.join(cell.get('source', []))
            html_content = markdown_to_html(source)
            current_slide.append(html_content)
        
        elif cell['cell_type'] == 'code':
            # Check for image outputs
            outputs = cell.get('outputs', [])
            for output in outputs:
                if 'data' in output:
                    if 'image/png' in output['data']:
                        img_data = output['data']['image/png']
                        current_slide.append(f'<img src="data:image/png;base64,{img_data}" alt="Chart">')
                    elif 'text/html' in output['data']:
                        current_slide.append(''.join(output['data']['text/html']))
                    elif 'text/plain' in output['data']:
                        text = ''.join(output['data']['text/plain'])
                        current_slide.append(f'<pre>{escape_html(text)}</pre>')
    
    # Close last slide
    if current_slide:
        html_parts.append('<div class="slide">')
        html_parts.append('<div class="content">')
        html_parts.extend(current_slide)
        html_parts.append('</div></div>')
        slide_num += 1
    
    # Add JavaScript for navigation
    html_parts.append(f"""
    <script>
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        const totalSlides = {slide_num};
        
        function updateSlideNum() {{
            document.getElementById('slideNum').textContent = `${{currentSlide + 1}} / ${{totalSlides}}`;
        }}
        
        function showSlide(n) {{
            if (n >= slides.length) n = 0;
            if (n < 0) n = slides.length - 1;
            currentSlide = n;
            slides.forEach((slide, i) => {{
                slide.style.display = i === n ? 'flex' : 'none';
            }});
            updateSlideNum();
        }}
        
        function nextSlide() {{
            showSlide(currentSlide + 1);
        }}
        
        function previousSlide() {{
            showSlide(currentSlide - 1);
        }}
        
        // Keyboard navigation
        document.addEventListener('keydown', (e) => {{
            if (e.key === 'ArrowRight' || e.key === ' ') nextSlide();
            if (e.key === 'ArrowLeft') previousSlide();
        }});
        
        // Initialize
        showSlide(0);
    </script>
</body>
</html>""")
    
    # Write HTML file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html_parts))
    
    print(f"✓ HTML presentation created: {output_path.absolute()}")
    print(f"  Total slides: {slide_num}")
    print(f"\nTo view in browser:")
    print(f"  open {output_path.absolute()}")
    
    return True

if __name__ == "__main__":
    import sys
    success = create_html_presentation()
    sys.exit(0 if success else 1)

