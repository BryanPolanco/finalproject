#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
import jinja2
import os
import urllib
from google.appengine.api import users
from google.appengine.api import urlfetch
from apiclient.discovery import build
from optparse import OptionParser
import logging
import random
import urllib2
import json


DEVELOPER_KEY = "AIzaSyAK_0glv6MteAUDzFCa9vd8q0d6ETePcw0"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        greeting = ('<a href = "%s">Sign in or register</a>.' %
            users.create_login_url('/drop'))
        self.response.write('<html><body>%s</body></html>' % greeting)
        template = JINJA_ENVIRONMENT.get_template('sign_in.html')
        self.response.write(template.render())

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        # greeting = ('Welcome, %s! (<a href=%s>sign_out</a>)' %
        #     (user.nickname(), users.create_logout_url('/')))
        # self.response.write('<html><body>%s</body></html>' % greeting)

        youtube = build(
            YOUTUBE_API_SERVICE_NAME,
            YOUTUBE_API_VERSION,
            developerKey=DEVELOPER_KEY)
        search_response = youtube.search().list(
            q = self.request.get('query'),
            part="id,snippet",
            maxResults = 50
        ).execute()

        videos = []
        video_collection = []
        video_count = 3
        for search_result in search_response.get("items", []):
            videos.append(search_result)
        for vid in range(video_count):
            randomindex = random.randint(0,len(videos)-1)
            cool_video = videos[randomindex]
            video_collection += [cool_video]
        #now is instagram
        counter = 4
        url = ('https://api.instagram.com/v1/media/popular?'
            'access_token=145068709.1fb234f.d0a68e4a96fd44fba1b9082101de0e3b')
        collection = [ ]
        x=0
        for i in range(counter):
            string = urllib2.urlopen(url)
            bigdictionary = json.loads(string.read())
            picture = bigdictionary['data'][x]['link']
            collection += [picture]
            x += 1
        logging.info(collection)

        template_values = {'video_collection': video_collection, 'collection': collection}
        self.response.headers['Content-type'] = 'text/html'
        template = JINJA_ENVIRONMENT.get_template('Templates/drop.html')
        self.response.write(template.render(template_values))


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

app = webapp2.WSGIApplication([
    ('/drop', MainHandler),
    ('/', LoginHandler)
], debug=True)
