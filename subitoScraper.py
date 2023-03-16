import requests
import bs4
import webbrowser

LINK = "https://www.subito.it/annunci-italia/vendita/informatica/?q=macbook&o="
PRE_LINK = "https://www.subito.it/informatica/"
QUERY = "macbook-"
NOT_QUERY = ['barbie-', 'wrangler-', 'thun-', 'magico-', 'magica-', 'amuleto-', 'radiocomandata-', 'bambola-', 'autovox-', 'kinder-', 'disney-', 'yu-gi-oh-', 'yugioh-', 'pokemon-', 'telefono-',
			'calciatori-', 'jasmine-']
i = 0
f = 0
links = []
while i < 3:
	LINK_ = LINK + str(i)
	res = requests.get(LINK_)
	if res:
		soup = bs4.BeautifulSoup(res.text, 'html.parser')
		sub_soup = soup.find('div', class_='container ItemListContainer_container__SjEc1')
		a_soup = sub_soup.find_all('a')
		for link in a_soup:
			link_ = str(link.get('href'))
			if PRE_LINK in link_:
				for query in NOT_QUERY:
					if query in link_:
						f = 0
						break 
					else:
						f = 1
				if f == 1 and QUERY in link_:
					links.append(link_)
		i += 1
	else:
		print("Page not found!")
for link in links:
	#res = requests.get(link)
	#soup = bs4.BeautifulSoup(res.text, 'html.parser')
	#title = soup.title.string
	print(link)


