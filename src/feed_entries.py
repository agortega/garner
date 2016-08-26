import feedparser

def get_feed_entries(url):
    """
    Get links found in the RSS feed by entering the URL for the feed.
    :param url: RSSS feed from a url
        TODO: Create abstraction for url:
            Example: https://news.google.com/news/feeds?cf=all&ned=us&hl=en&q=YOUR_QUERY_HERE&output=rss
        Parameters can be adjusted according to GET requests
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