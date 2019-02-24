[![](https://img.shields.io/pypi/pyversions/github-topics.svg?longCache=True)](https://pypi.org/project/github-topics/)
[![](https://img.shields.io/pypi/v/github-topics.svg?maxAge=3600)](https://pypi.org/project/github-topics/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/github-topics.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/github-topics.py/)

#### Install
```bash
$ [sudo] pip install github-topics
```

#### Config
bash|python
-|-
`export GITHUB_TOKEN="your_github_token"`|`os.environ["GITHUB_TOKEN"]="your_github_token"`

#### Functions
function|`__doc__`
-|-
`github_topics.add(fullname, topics)`|add repo topics
`github_topics.clear(fullname)`|remove all repo topics
`github_topics.get(fullname)`|return list of repo topics
`github_topics.replace(fullname, topics)`|replace repo topics
`github_topics.rm(fullname, topics)`|remove repo topics

#### CLI
usage|`__doc__`
-|-
`python -m github_topics.add fullname topics ...`|add repo topics
`python -m github_topics.clear fullname`|remove all repo topics
`python -m github_topics.get fullname`|print repo topics
`python -m github_topics.remove fullname topics ...`|remove repo topics
`python -m github_topics.replace fullname topics ...`|set repo topics

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>