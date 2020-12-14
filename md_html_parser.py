import os
import markdown
from bs4 import BeautifulSoup

md_file = ""

files_list = []

def get_files_list(dir):
    global files_list
    for root, dirs, files in os.walk(dir, topdown=False):
        for file in files:
            name, suf = os.path.splitext(file)
            if suf == ".md":
                files_list.append(os.path.join(root, file))
    return files_list

def read_md(md_file):
    with open(md_file, "r", encoding="utf-8") as file:
        text = file.read()
        html = markdown.markdown(text)
        imgs_list = html_parser(html)
        for img in imgs_list:
            write_in(md_file, img)
    return

def html_parser(html_text):
    imgs_list = []
    soup = BeautifulSoup(html_text, features="html.parser")
    tags = soup.find_all("img")
    for tag in tags:
        if tag.attrs["src"]:
            imgs_list.append(tag["src"])
    return imgs_list

def write_in(file_name, img_name):
    output_txt.write(file_name + "\t" + img_name + "\n" )
    return



md_file = input(">>> Pleae input a location: ")
print("\n" + "================ Start ===================" + "\n")

# Check if the directory is complete
if md_file.endswith("\\"):
    pass
else:
    md_file = md_file + "\\"

if os.access(md_file, os.R_OK):
    print("Loading " + md_file + "\n")
else:
    print("Cannot access or write in: " + md_file + "\n")

output_txt = open(md_file + "img_info.txt", "w")

file_list = get_files_list(md_file)

for file in file_list:
    read_md(file)

output_txt.close()

print("================ Done :) ================")