import uuid
from shutil import copyfile
from random import shuffle

PAGE_COUNT = 500
REFERENCE_COUNT = 5
FLAG = "FLAG-CR33PYCR4WLIES"

class Page:
    def __init__(self):
        self.is_index = False
        self.is_flag = False
        self.id = uuid.uuid4().hex
        self.links = []

page_ids = []

for i in range(PAGE_COUNT):
    page_ids.append(Page())

page_ids[0].is_index = True
page_ids[-1].is_flag = True

for i in range(REFERENCE_COUNT):
    page_ids_unused = [p for p in page_ids]
    shuffle(page_ids_unused)
    for page in page_ids:
        page.links.append(page_ids_unused.pop())

for page in page_ids:
    page_file = f"./pages/{page.id}.html"
    if page.is_index:
        page_file = "./pages/index.html"
    copyfile("./template.html", page_file)
    contents = ""
    with open(page_file, "r") as f:
        for line in f:
            contents += line
    contents = contents.replace("{{id}}", page.id)
    links = ""
    for link in page.links:
        links += f"<a href=\"./{link.id}.html\"/>{link.id}</a>\n"
    if page.is_flag:
        links += f"{FLAG}\n"
    contents = contents.replace("{{links}}", links)
    with open(page_file, "w") as f:
        f.write(contents)


