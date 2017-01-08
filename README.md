# Ferrite

Ferrite is like Google, but for your browser history.
Ferrite is a full-text search engine for your browsing history.
Ferrite is love. Ferrite is life.

# Hum ?

Ferrite works in 2 parts. One part that runs in your browser (Firefox for now, but it's a webExtension so it might work in Chrome) and collects every web page you visit. It grabs it's URL, DOM and a timestamp and then periodically sends it to the Python.

The Python part is an HTTP server that waits for the JS to call. Right now, the Python doesn't do anything more than printing every URL to stdout but it's Python, it can do EVERYTHING !

![xkcd python comic](https://imgs.xkcd.com/comics/python.png)


Howto : [install the extension in your browser](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Your_first_WebExtension#Installing)

# Why Ferrite ?

Because [magnetic-core memory](https://en.wikipedia.org/wiki/Magnetic-core_memory) uses ferrite cores to store information and it's a cool name.

![A ferrite core memory](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/KL_CoreMemory.jpg/260px-KL_CoreMemory.jpg)

# Disclaimer

Ferrite stores your private/incognito browsing history, beware !

Why does ferrite do that ? Because i did not find a way to known if a content script was loaded in an incognito tab or not...
