from scrapy import cmdline
name = 'car'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())