import setuptools

setuptools.setup(
    name='github-topics',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
