"""
    URLResolver Addon for Kodi
    Copyright (C) 2016 t0mm0, tknorris

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import functools
import log_utils
import time
import pickle
import hashlib
import os
import shutil

def reset_cache():
    print "test"
    
def _get_func(name, args=None, kwargs=None, cache_limit=1):
    print "test"
    
def _save_func(name, args=None, kwargs=None, result=None):
    print "test"

def _get_filename(name, args, kwargs):
    print "test"

def cache_method(cache_limit):
    print "test"

def cache_function(cache_limit):
    print "test"
