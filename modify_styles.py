import re

with open('styles.css', 'r') as f:
    css = f.read()

# 1. Colors & Variables
css = css.replace('--bg-color: #080808;', '--bg-color: #F4F4F6;')
css = css.replace('--card-bg: rgba(20, 20, 20, 0.6);', '--card-bg: rgba(255, 255, 255, 0.9);')
css = css.replace('--card-border: rgba(255, 255, 255, 0.08);', '--card-border: rgba(0, 0, 0, 0.04);\n  --card-shadow: 0 8px 32px rgba(0, 0, 0, 0.04);')
css = css.replace('--text-primary: #ffffff;', '--text-primary: #1A1A1A;')
css = css.replace('--text-secondary: #a0a0a0;', '--text-secondary: #666666;')
css = css.replace('--accent-glow: rgba(255, 102, 0, 0.25);', '--accent-glow: rgba(255, 102, 0, 0.15);')

css = css.replace('--radius-card: 24px;', '--radius-card: 32px;')

# 2. Body Grid Pattern
css = css.replace('linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px)', 'linear-gradient(rgba(0, 0, 0, 0.03) 1px, transparent 1px)')

# 3. Blobs (Make them softer for light mode)
css = css.replace('filter: blur(100px);', 'filter: blur(120px);')
css = css.replace('opacity: 0.15;', 'opacity: 0.25;')
css = css.replace('opacity: 0.08;', 'opacity: 0.15;')

# 4. Marquee Borders
css = css.replace('border-top: 1px solid rgba(255, 255, 255, 0.05);', 'border-top: 1px solid rgba(0, 0, 0, 0.05);')
css = css.replace('border-bottom: 1px solid rgba(255, 255, 255, 0.05);', 'border-bottom: 1px solid rgba(0, 0, 0, 0.05);')

# 5. Bento Card Box Shadows
css = css.replace('transition: all 0.4s var(--anim-ease);\n}', 'transition: all 0.4s var(--anim-ease);\n  box-shadow: var(--card-shadow);\n}')
css = css.replace('border-color: rgba(255, 255, 255, 0.2);\n  box-shadow: 0 20px 50px -10px rgba(0, 0, 0, 0.3);', 'border-color: var(--accent-color);\n  box-shadow: 0 20px 40px -10px rgba(255, 102, 0, 0.15);')

# 6. Hero Image
css = css.replace('border: 2px solid rgba(255, 255, 255, 0.1);', 'border: 4px solid #FFFFFF;')

# 7. Personal Card
css = css.replace('background: linear-gradient(135deg, rgba(255, 102, 0, 0.08), transparent);', 'background: linear-gradient(135deg, rgba(255, 102, 0, 0.08), rgba(255, 255, 255, 0.8));')

# 8. Service Items
css = css.replace('background: rgba(255, 255, 255, 0.03);', 'background: rgba(0, 0, 0, 0.02);')
css = css.replace('background: rgba(255, 255, 255, 0.06);', 'background: #FFFFFF;')

# 9. LinkedIn Button
css = css.replace('background: #000;\n  color: var(--accent-color);', 'background: #FFFFFF;\n  color: var(--accent-color);')

# 10. Resume Lines
css = css.replace('border-bottom: 1px solid rgba(255, 255, 255, 0.08);', 'border-bottom: 1px solid rgba(0, 0, 0, 0.06);')
css = css.replace('background: rgba(255, 255, 255, 0.05);\n  color: #ccc !important;', 'background: rgba(0, 0, 0, 0.03);\n  color: #555 !important;')
css = css.replace('color: #bbb !important;', 'color: #666 !important;')

# 11. Footer
css = css.replace('color: #bdbdbd;', 'color: #777777;')
css = css.replace('background: rgba(255, 255, 255, 0.08);', 'background: rgba(0, 0, 0, 0.04);')
css = css.replace('border: 1px solid rgba(255, 255, 255, 0.1);', 'border: 1px solid rgba(0, 0, 0, 0.04);')
css = css.replace('color: #e0e0e0;', 'color: #333333;')
css = re.sub(r'\.footer-nav a:hover \{\n\s+background-color: var\(--accent-color\);\n\s+color: #000;\n\}', '.footer-nav a:hover {\n  background-color: var(--accent-color);\n  color: #FFF;\n}', css)
css = css.replace('background: rgba(255, 255, 255, 0.05);', 'background: rgba(0, 0, 0, 0.03);')

with open('styles.css', 'w') as f:
    f.write(css)

print("Styles updated")
