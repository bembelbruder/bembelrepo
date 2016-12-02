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
import urllib
import urlparse
import sys
import os
import re
import time
import log_utils

def get_path():
    print "test"
    
def get_profile():
    print "test"

def translate_path(path):
    print "test"

def set_setting(id, value):
    print "test"

def get_version():
    print "test"

def get_id():
    print "test"

def get_name():
    print "test"

def open_settings():
    print "test"

def get_plugin_url(queries):
    print "test"

def end_of_directory(cache_to_disc=True):
    print "test"

def set_content(content):
    print "test"
    
def create_item(queries, label, thumb='', fanart='', is_folder=None, is_playable=None, total_items=0, menu_items=None, replace_menu=False):
    print "test"

def add_item(queries, list_item, fanart='', is_folder=None, is_playable=None, total_items=0, menu_items=None, replace_menu=False):
    print "test"

def parse_query(query):
    print "test"

def notify(header=None, msg='', duration=2000, sound=None):
    print "test"

def close_all():
    print "test"
        
def get_current_view():
    print "test"

class WorkingDialog(object):
    def __init__(self):
        print "test"
    
    def __enter__(self):
        print "test"
    
    def __exit__(self, type, value, traceback):
        print "test"

def has_addon(addon_id):
    print "test"

class ProgressDialog(object):
    def __init__(self, heading, line1='', line2='', line3='', background=False, active=True, timer=0):
        print "test"

    def __create_dialog(self, line1, line2, line3):
        print "test"
        
    def __enter__(self):
        print "test"
    
    def __exit__(self, type, value, traceback):
        print "test"
    
    def is_canceled(self):
        print "test"
        
    def update(self, percent, line1='', line2='', line3=''):
        print "test"

class CountdownDialog(object):
    def __init__(self, heading, line1='', line2='', line3='', active=True, countdown=60, interval=5):
        print "test"

    def __enter__(self):
        print "test"
    
    def __exit__(self, type, value, traceback):
        print "test"
    
    def start(self, func, args=None, kwargs=None):
        print "test"
    
    def is_canceled(self):
        print "test"
        
    def update(self, percent, line1='', line2='', line3=''):
        print "test"
