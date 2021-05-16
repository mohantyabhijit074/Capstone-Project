from newspaper import Article
 
url = "https://www.msn.com/en-in/news/newsindia/india-registers-326098-new-covid-19-cases-3980-deaths-in-last-24-hours/ar-BB1gKP2m?li=AAggbRN" 
# download and parse article
article = Article(url)
article.download()
article.parse()
 
# print article text
print(article.text)
