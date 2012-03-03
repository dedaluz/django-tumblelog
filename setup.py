from setuptools import setup, find_packages
from tumblelog import __version__

setup(
    name='django-tumblelog',
    version=__version__,
    description='A simple and extensible tumblelog engine for Django',
    keywords='django, blog, tumblelog, tumblr',
    author='Chuck Harmston',
    author_email='chuck@chuckharmston.com',
    url='https://github.com/chuckharmston/django-tumblelog',
    license='MIT',
    package_dir={
        'tumblelog': 'tumblelog',
    },
    packages=find_packages(),
    install_requires=[
        'python-oembed==0.2.1',
        'PIL',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Communications",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary",
    ],
)
