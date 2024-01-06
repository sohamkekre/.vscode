import requests
from bs4 import BeautifulSoup
with open("Beautiful soap/sample.html","r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc,"html.parser")
# print(soup)
# print(f"To print html title tag {soup.title}, 
#         To print html title name: {soup.title.name}, 
#         To print html's title: {soup.title.string} ")
# print(f"To print div: {soup.div}")
# print(f"To print heading: {soup.h1.string}")

# Now if we want to print all the div content
# find_all=(soup.find_all("div"))
# find_all=(soup.find_all("div")[1])
# print(f"To print find_all: {find_all}")

# for child in soup.find(class_="container").children:
#     print(child)

# for parent in soup.find(class_ = "container").parent:
#     print(parent)
    
# cont = soup.find(class_ = "container")
# cont.name = "span"
# cont["class"] = "my_class"
# cont.string = "I am a string"
# print(cont)

ulTag = soup.new_tag("ul")

liTag = soup.new_tag("li")
liTag.string = "Home"
ulTag.append(liTag)

liTag = soup.new_tag("li")
liTag.string = "About"
ulTag.append(liTag)

soup.body.insert(0,ulTag)
with open("Beautiful soap/sample.html","w") as f:
    f.write(str(soup))