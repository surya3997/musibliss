from bs4 import BeautifulSoup

import requests

#url = raw_input("Enter a website to extract the URL's from: ")

domain = "https://www.sunmusiq.com"
sub_dirs = ["/search/search-for-blocked-movies-starmusiq-sort-by-$.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-a.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-b.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-c.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-d.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-e.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-f.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-g.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-h.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-i.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-j.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-k.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-l.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-m.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-n.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-o.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-p.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-q.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-r.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-s.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-t.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-u.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-v.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-w.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-x.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-y.html",
"/search/search-for-blocked-movies-starmusiq-sort-by-z.html"]


for sub_dir in sub_dirs:
	url = domain + sub_dir
	r  = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data)
	for link in soup.find_all('a'):
		valid_url = link.get('href')
		if "/movie/" in valid_url:
			print(valid_url)
