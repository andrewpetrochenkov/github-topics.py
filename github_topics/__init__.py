__all__ = ['add', 'clear', 'get', 'replace', 'rm']


import github
import os


def _get_repo(fullname):
    g = github.Github(os.environ["GITHUB_TOKEN"])
    if "/" in fullname:
        return g.get_repo(fullname)
    return g.get_user().get_repo(fullname)


def get(fullname):
    """return a list of repo topics"""
    return _get_repo(fullname).get_topics()


def replace(fullname, topics):
    """replace repo topics"""
    return _get_repo(fullname).replace_topics(list(topics))


def add(fullname, topics):
    """add repo topics"""
    old_topics = get(fullname)
    new_topics = list(set(list(old_topics) + list(topics)))
    replace(fullname, new_topics)


def rm(fullname, topics):
    """remove repo topics"""
    old_topics = get(fullname)
    new_topics = list(set(old_topics) - set(topics))
    replace(fullname, new_topics)


def clear(fullname):
    """remove all repo topics"""
    replace(fullname, [])
