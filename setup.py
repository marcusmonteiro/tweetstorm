from setuptools import setup, find_packages
import tweetstorm

INSTALL_REQUIRES = [
    'tweepy', 'nltk'
]

setup(
    name='tweetstorm',
    version=tweetstorm.__version__,
    description=tweetstorm.__doc__.strip(),
    download_url='https://github.com/marcusmonteiro/tweetstorm',
    author=tweetstorm.__author__,
    author_email='mvsouza007@gmail.com',
    license=tweetstorm.__license__,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tweetstorm = tweetstorm.__main__:main'
        ]
    },
    install_requires=INSTALL_REQUIRES
)
