[Scrapy笔记02- 完整示例](https://www.xncoding.com/2016/03/10/scrapy-02.html)

直接运行例子，得到500的错误，通过浏览器调试，抓取请求，得到headers信息后，
在 spiders/huxiu\_spider.py 中添加了

       def start_requests(self):
        start_urls = [
            "https://www.huxiu.com/"
        ]

        print "pengcz starting crawl"
        for url in start_urls:
            yield scrapy.Request(url,
                    headers = {
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US,en;q=0.9'
                    },
                callback = self.parse)

