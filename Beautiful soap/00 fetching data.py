import requests

# url = "https://www.tutorialspoint.com/computer_graphics/2d_transformation.htm"
# r = requests.get(url)
# print(r.text)

def FetchAndSaveToFile(url,path):
    r = requests.get(url)
    with open(path,"w") as f:
        f.write(r.text)

url="https://api.nobelprize.org/v1/prize.json"
FetchAndSaveToFile(url, "C:/Users/soham/.vscode/text.html")