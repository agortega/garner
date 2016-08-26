""" Methods for Regex Operations """
import re


def get_ncl(link):
    """
    Parse the NCL value from a url in a news story.
    :param link: Link containing the NCL value (NCL: News Coverage Link, it is an ID for a news event)
        Example:
            u'https://news.google.com/news/more?ncl=dqCs5-0uTivFQMM-rmkoZU6mz9QnM&' : Describes the coverage of the earthquake
    :return: the hashcode for the story
    """
    ncl_string = re.findall("ncl=.*?&", link)
    if ncl_string:
        return ncl_string[0][4:-1]
    else:
        return ''