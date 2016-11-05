#!/usr/bin/python
from mediawiki import MediaWiki
import subprocess

wikipedia = MediaWiki()
rndm = wikipedia.random(pages=1)
p = wikipedia.page(rndm)

txt = p.summarize(sentences=2)
p1 = subprocess.Popen(["echo", txt], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["cowsay"], stdin=p1.stdout, stdout=subprocess.PIPE)

print p.title
print p2.stdout.read()
print p.url
