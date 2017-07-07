from setuptools import setup


version = "1.0.0"
url = "https://github.com/TadLeonard/fuckpad"
download = "{}/archive/{}.tar.gz".format(url, version)
description = "Disables the loathsome Synaptics touchpad"
long_description = """
Disable the loathsome Synaptics touchpad with ease
==================================================
Synaptics touchpads don't work well on Linux without lots of
careful configuration. This tool makes it easy to disable them.

Documentation
=============
See {url} for more.""".format(url=url)


classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Programming Language :: Python :: 3',
  'Programming Language :: Python :: 2',
]


setup(name="fuckpad",
      version=version,
      py_modules=["fuckpad"],
      scripts=["fuckpad"],
      url=url,
      description=description,
      long_description=long_description,
      classifiers=classifiers,
      author="Tad Leonard",
      author_email="tadfleonard@gmail.com",
      download_url=download
)
