import feedparser

def get_feed_entries(url):
    """
    Get links found in the RSS feed by entering the URL for the feed.
    :param url: RSSS feed from a url
    :return: A list of links in the RSS feed
    """
    links = []
    try:
        doc = feedparser.parse(u'https://news.google.com/news?cf=all&hl=en&pz=1&ned=au&output=rss')
        for feed in doc.entries:
            links.append(str(feed.link))
    except:
        pass
    return links