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
import urllib2
import json
import logging

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja2_environment.get_template('Templates/drop.html')
        self.response.write(template.render())

class InstaHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja2_environment.get_template('Templates/drop.html')
        logging.info("HELLLO")
        counter = 4
        url = ('https://api.instagram.com/v1/media/popular?'
            'access_token=145068709.1fb234f.d0a68e4a96fd44fba1b9082101de0e3b')
        collection = [ ]
        x=0
        for i in range(counter):
            logging.info("HEHEHHEHEHHEHE")
            string = urllib2.urlopen(url)
            bigdictionary = json.loads(string.read())
            picture = bigdictionary['data'][x]['link']
            collection += [picture]
            x += 1
        logging.info(collection)
        template_vars = {'collection':collection}
        self.response.write(template.render(template_vars))

jinja2_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/insta', InstaHandler)
], debug=True)
