import re

with open('styles.css', 'r') as f:
    css = f.read()

# Replace "body.light-mode, html.light-mode-pre body" with "html.light-mode body"
css = css.replace('body.light-mode, html.light-mode-pre body', 'html.light-mode body')

with open('styles.css', 'w') as f:
    f.write(css)

