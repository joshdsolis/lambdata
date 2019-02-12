#!/USR/BIN/ENV PYTHON
""" Package setup/installation and emtadata for lambdata
"""

import setuptools

REQUIRED = [
	"numpy",
	"pandas",
]

with open("README.md", "r") as fh:
	LONG_DESCRIPTION = fh.read()

setuptools.setup(
	name = "lambdata-joshdsolis",
	version= "0.0.4",
	author ="joshdsolis",
	description="A collection of Data Science helper functions",
	long_description = LONG_DESCRIPTION,
	long_description_content_type = "text/markdown",
	url = "https://github.com/joshdsolis/lambdata",
	packages=setuptools.find_packages(),
	python_requires = ">=3.5",
	install_requires=REQUIRED,
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
      	  	"Operating System :: OS Independent",
    ]
)
