import requests
import bs4
response = requests.get('https://dantri.com.vn/nhip-song-tre/ranh-bung-sau-hun-hut-cua-chi-em-viet-khien-dan-ong-me-met-20181110123833625.htm')
#print(response.content.decode())
soup = bs4.BeautifulSoup(response.content.decode(), 'html.parser')
#
    #f.write(response.content.decode())
print(soup.title)
all_div = soup.find_all("div",{date-boxtype":"time})
print(len(all_div))
result = []
for v in all_div:
    result.append(v.div.h2.a.string)
first = all_div[0]
print(firtst.div.h2.a.string)
