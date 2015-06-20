from bs4 import BeautifulSoup
import urllib2

raw = []
result = []
url = "https://sat.collegeboard.org/register/sat-us-dates"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
table = soup.find("table", {"class": "vcalendar tableMain"})
sub = table.findAll("tr", {"class": "vevent center"})

for subb in sub:
	raw.append(subb.find("td", {"class": "bold"}))
for unclean_dates in raw:
	result.append(unclean_dates.contents[0].strip() + " " + unclean_dates.contents[2].strip())

print result
