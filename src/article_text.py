from newspaper import Article



def get_article_text(link):
    """
    Method to extract article text
    :param link: News URL Link, like 'http://www.bbc.co.uk/zhongwen/simp/chinese_news/2012/12/121210_hongkong_politics.shtml
        Example Strings:
            u'http://www.bbc.co.uk/zhongwen/simp/chinese_news/2012/12/121210_hongkong_politics.shtml'
            u'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
    :return: Body Text for the article
    """
    try:
        article = Article(link)
        article.download()
        article.parse()
    except:
        return None
    return article.text.encode("utf8")