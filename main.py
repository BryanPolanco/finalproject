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
from google.appengine.api import urlfetch
from apiclient.discovery import build
from optparse import OptionParser
import logging
import random



DEVELOPER_KEY = "AIzaSyAK_0glv6MteAUDzFCa9vd8q0d6ETePcw0"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

class MainHandler(webapp2.RequestHandler):
    def get(self):
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

        for search_result in search_response.get("items", []):
            videos.append(search_result)
        randomindex = random.randint(0,len(videos)-1)
        video = videos[randomindex]

        template_values = {'video': video}
        self.response.headers['Content-type'] = 'text/html'
        template = JINJA_ENVIRONMENT.get_template('Templates/drop.html')
        self.response.write(template.render(template_values))



JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])
app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
