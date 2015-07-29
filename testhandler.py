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

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import webapp2
import jinja2
import os


#
# DEVELOPER_KEY = "AIzaSyAK_0glv6MteAUDzFCa9vd8q0d6ETePcw0"
# YOUTUBE_API_SERVICE_NAME = "youtube"
# YOUTUBE_API_VERSION = "v3"

class TestHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("hello")
        # template = jinja2_environment.get_template('Templates/drop.html')
        # self.response.write(template.render())

  #   def youtube_search(options):
  #       youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
  #           developerKey=DEVELOPER_KEY)
  #
  # # Call the search.list method to retrieve results matching the specified
  # # query term.
  #       search_response = youtube.search().list(
  #           q = options.q,
  #           type = 'video',
  #           part = "id,snippet",
  #           location = options.location,
  #           locationRadius = options.location_radius,
  #           maxResults=options.max_results
  #           ).execute()
  #
  #       search_videos = []
  #
  #       for search_result in search_response.get("items", []):
  #           search_videos.append(search_result["id"]["videoId"])
  #       video_ids = ",".join(search_videos)
  #
  #       video_response = youtube.videos().list(
  #           id=video_ids,
  #           part='snippet, recordingDetails'
  #       ).execute()
  #
  #       videos = []
  #
  #       for video_result in video_response.get("items", []):
  #           videos.append("%s, (%s,%s)" % (video_result["snippet"]["title"],
  #                             video_result["recordingDetails"]["location"]["latitude"],
  #                             video_result["recordingDetails"]["location"]["longitude"]))
  #
  #       print "Videos:\n", "\n".join(videos), "\n"
  #
  #
  #   if __name__ == "__main__":
  #       argparser.add_argument("--q", help="Search term", default="Google")
  #       argparser.add_argument("--location", help="Location", default="37.42307,-122.08427")
  #       argparser.add_argument("--location-radius", help="Location radius", default="5km")
  #       argparser.add_argument("--max-results", help="Max results", default=25)
  #       args = argparser.parse_args()
  #
  #       try:
  #           youtube_search(args)
  #       except HttpError, e:
  #           print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
  #
  # # Add each result to the appropriate list, and then display the lists of
  # # matching videos, channels, and playlists.
  #       for search_result in search_response.get("items", []):
  #           if search_result["id"]["kind"] == "youtube#video":
  #               videos.append("%s (%s)" % (search_result["snippet"]["title"],
  #                                search_result["id"]["videoId"]))
  #
  #       print "Videos:\n", "\n".join(videos), "\n"
  #
  #
  #   if __name__ == "__main__":
  #       argparser.add_argument("--q", help="Search term", default="Google")
  #       argparser.add_argument("--max-results", help="Max results", default=25)
  #       args = argparser.parse_args()
  #
  #   try:
  #       youtube_search(args)
  #   except HttpError, e:
  #       print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

# jinja2_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/test', TestHandler)
], debug=True)
