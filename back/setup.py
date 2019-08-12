#!/usr/bin/env python
# -*- coding: utf-8 -*-

import versiontools_support
from setuptools import setup, find_packages

setup(
    name = 'tuesmon-contrib-slack',
    version = ":versiontools:tuesmon_contrib_slack:",
    description = "The Tuesmon plugin for slack integration",
    long_description = "",
    keywords = 'tuesmon, slack, integration',
    author = 'Jesús Espino García',
    author_email = 'jesus.espino@kaleidos.net',
    url = 'https://github.com/tuesmoncom/tuesmon-contrib-slack',
    license = 'AGPL',
    include_package_data = True,
    packages = find_packages(),
    install_requires=[],
    setup_requires = [
        'versiontools >= 1.9',
    ],
    classifiers = [
        "Programming Language :: Python",
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
