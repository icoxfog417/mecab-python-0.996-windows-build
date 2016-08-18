#!/usr/bin/env python

from distutils.core import setup,Extension,os
import string

def cmd1(str):
    return os.popen(str).readlines()[0][:-1]

def cmd2(str):
    return string.split (cmd1(str))

setup(name = "mecab-python",
	version = "0.996",
	py_modules=["MeCab"],
	ext_modules = [
		Extension("_MeCab",
			["MeCab_wrap.cxx",],
			include_dirs=["C:/Program Files/MeCab/sdk"],
			library_dirs=["C:/Program Files/MeCab/sdk"],
			libraries=["libmecab"])
			])
