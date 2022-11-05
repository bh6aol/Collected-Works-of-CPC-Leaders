# Download Collected Works of CPC Leaders
# author: bh6aol <bh6aol@gmail.com>
# date: 2022-11-04 22:19

from bs4 import BeautifulSoup
import requests

ls = [
    {
        "name": "mzd",
        "size":4
    },
    {
        "name": "dxp",
        "size":3
    },
    {
        "name": "jzm",
        "size":3
    },
    {
        "name": "hjt",
        "size":3
    },
]
for l in ls:
    for v in range(1,l['size']+1):

        with open(f"./html/{l['name']}.vol.{v}.html",mode='r',encoding="utf-8") as f:
            soup = BeautifulSoup(f,"html.parser")
            lis = soup.find_all("li")
            idx = 1
            for li in lis:
                spans = li.a.find_all("span")
                title = spans[0].text
                link = spans[1].text
                print(f"[INFO] Downloading {l['name']} -> {v}.{idx}.{title}.mp3 ({idx}/{len(lis)})")
                response = requests.get(link)
                with open(f"./{l['name']}/{v}.{idx}.{title}.mp3","wb") as file:
                    file.write(response.content)
                idx += 1
            print(f"[INFO] Vol {v} Done")
    print(f"[INFO] {l['name']} Done")
print(f"[INFO] All Done")