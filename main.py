import requests

from bs4 import BeautifulSoup





class jobs:

    def __init__(self):
        self.links = set()
        self.bing_n = []

    def bing_results(self):
        i = 0
        while True:

            i+= 11
            if i >=  1000:
                break
            r = requests.get('https://www.bing.com/search?q=site%3asa+%22upload+cv%22&qs=HS&pq=site%3a&sc=8-5&cvid=D4D138F1557A4DCEAFF2D95845E54B64&sp=1&first={}'.format(i) , headers={'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:100.0) Gecko/20100101 Firefox/100.0"})

            self.bing_n.append(r.url)



    def whynot(self , link):
        try:
            r = requests.get(link).content
            return True , link if "upload" or "email" in r.lower() else False
        except:pass




    def get_jobs(self):
        print('Good , Working on it !!')
        for l in self.bing_n:
            r = requests.get(l, headers={'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:100.0) Gecko/20100101 Firefox/100.0"})
            soup = BeautifulSoup(r.content , 'lxml')
            for x in soup.find_all('div' , class_='b_attribution'):
                f = x.text
                if f.startswith('https://') or f.startswith('http://') or f.endswith('.sa'):
                    self.links.add(f)
        for results in self.links:
            print(self.whynot(results))



if __name__ == '__main__':
    c = jobs()
    c.bing_results()
    w = c.get_jobs()
    print(w)
