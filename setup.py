from setuptools import setup

# Original Metadata:
#
# Metadata-Version: 2.1
# Name: akinator.py
# Version: 5.0.0
# Summary: An API wrapper for the online game, Akinator, written in Python
# Home-page: https://github.com/NinjaSnail1080/akinator.py
# Author: NinjaSnail1080
# Author-email: innuganti.ashwin@gmail.com
# License: MIT License
# Project-URL: Documentation, https://github.com/NinjaSnail1080/akinator.py/blob/master/README.rst
# Project-URL: Source, https://github.com/NinjaSnail1080/akinator.py
# Project-URL: Tracker, https://github.com/NinjaSnail1080/akinator.py/issues
# Project-URL: Say Thanks!, https://saythanks.io/to/innuganti.ashwin%40gmail.com
# Keywords: akinator api
# Platform: UNKNOWN
# Classifier: Programming Language :: Python :: 3
# Classifier: Programming Language :: Python :: 3.5
# Classifier: Programming Language :: Python :: 3.6
# Classifier: Programming Language :: Python :: 3.7
# Classifier: Programming Language :: Python :: 3.8
# Classifier: Programming Language :: Python :: 3.9
# Classifier: Development Status :: 5 - Production/Stable
# Classifier: Intended Audience :: Developers
# Classifier: Natural Language :: English
# Classifier: License :: OSI Approved :: MIT License
# Classifier: Operating System :: OS Independent
# Classifier: Topic :: Software Development :: Libraries
# Classifier: Topic :: Software Development :: Libraries :: Python Modules
# Classifier: Topic :: Internet
# Classifier: Topic :: Utilities
# Requires-Python: >=3.5.3
# Description-Content-Type: text/x-rst
# License-File: LICENSE.txt
# Requires-Dist: requests
# Provides-Extra: async
# Requires-Dist: aiohttp ; extra == 'async'
# Provides-Extra: fast_async
# Requires-Dist: aiohttp ; extra == 'fast_async'
# Requires-Dist: cchardet ; extra == 'fast_async'
# Requires-Dist: aiodns ; extra == 'fast_async'

setup(
    name="akinator.py",
    version="5.0.0",
    description="An API wrapper for the online game, Akinator, written in Python",
    url="https://github.com/Middledot/akinator.py-snapshot",
    author="NinjaSnail1080",
    license="MIT",
    project_urls={
        "Documentation": "https://github.com/Middledot/akinator.py-snapshot/blob/master/README.rst",
        "Source": "https://github.com/Middledot/akinator.py-snapshot",
    },
    keywords="akinator api",
    classifiers={
        "Classifier": "Programming Language :: Python :: 3",
        "Classifier": "Programming Language :: Python :: 3.5",
        "Classifier": "Programming Language :: Python :: 3.6",
        "Classifier": "Programming Language :: Python :: 3.7",
        "Classifier": "Programming Language :: Python :: 3.8",
        "Classifier": "Programming Language :: Python :: 3.9",
        "Classifier": "Development Status :: 5 - Production/Stable",
        "Classifier": "Intended Audience :: Developers",
        "Classifier": "Natural Language :: English",
        "Classifier": "License :: OSI Approved :: MIT License",
        "Classifier": "Operating System :: OS Independent",
        "Classifier": "Topic :: Software Development :: Libraries",
        "Classifier": "Topic :: Software Development :: Libraries :: Python Modules",
        "Classifier": "Topic :: Internet",
        "Classifier": "Topic :: Utilities"
    },
    python_requires='>=3.5.3',
    extra_requires={  # I don't actually know any specific versions so I'm just using the versions I already have
        "async": ["aiohttp>=3.8.1"],
        "fast_async": [
            "aiohttp>=3.8.1",
            "cchardet>=2.1.7",
            "aiodns>=3.8.1"
        ]
    },
    install_requires=["requests>=2.27.1"]
)
