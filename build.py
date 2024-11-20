from jinja2 import Environment, FileSystemLoader

import index

env = Environment(
    loader=FileSystemLoader("template"), trim_blocks=True, lstrip_blocks=True
)

template = env.get_template("index.html.j2")
output = template.render(
    head=index.head, bio=index.bio, moments=index.moments, galleries=index.galleries
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(output)
