import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#map_pick will set-up which map will be used by returning the url
#map0 will be a blank map that reads "ERROR, START AND END POINT CANNOT BE THE SAME"
#map 00 will be a blank map that reads "LOCATION ERROR"
def map_pick(location_one, location_two):
    if location_one == location_two:
        url = map0
    elif location_one == "Kellogg":
        if location_two == "USU":
            url = KellUSU
        if location_two == "Starbucks":
            url = KellStar
        if location_two == "SBSB":
            url = KellSBSB
        if location_two == "PS1":
            url = KellPS1
    elif location_one == "USU":
        if location_two == "Kellogg":
            url = KellUSU
        if location_two == "Starbucks":
            url = USUStar
        if location_two == "SBSB":
            url = USUSBSB
        if location_two == "PS1":
            url = USUPS1
    elif location_one == "Starbucks":
        if location_two == "Kellogg":
            url = KellStar
        if location_two == "USU":
            url = USUStar
        if location_two == "SBSB":
            url = StarSBSB
        if location_two == "PS1":
            url = StarPS1
    elif location_one == "SBSB":
        if location_two == "Kellogg":
            url = KellSBSB
        if location_two == "USU":
            url = USUSBSB
        if location_two == "Starbucks":
            url = StarSBSB
        if location_two == "PS1":
            url = SBSBPS1
    elif location_one == "PS1":
        if location_two == "Kellogg":
            url = KellPS1
        if location_two == "USU":
            url = USUPS1
        if location_two == "Starbucks":
            url = StarPS1
        if location_two == "SBSB":
            url = SBSBPS1
    else:
        url = map00
    return url

# # this the home page, using /home
class MainPage(webapp2.RequestHandler):
    def get(self):
        main_template = the_jinja_env.get_template('templates/index.html')
        self.response.headers['Content-Type'] = 'html'
        self.response.write(main_template.render())

# # this the map page, using /fastestpath
class FastPage(webapp2.RequestHandler):
    def get(self):
        end_template = the_jinja_env.get_template('templates/map.html')
        self.response.headers['Content-Type'] = 'html'
        the_variable_dict = {
            "img_url": "map_url"
        }
        self.response.write(end_template.render(the_variable_dict))

    def post(self):
        results_template = the_jinja_env.get_template('templates/map.html')
        location_one = self.request.get('starting point')
        location_two = self.request.get('destination')
        map_url = map_pick(location_one, location_two)
        the_variable_dict = {
            "img_url": "map_url"
        }
        self.response.write(results_template.render(the_variable_dict))

# class MapPage(webapp2.RequestHandler):
#     def get(self):
#         map_template = the_jinja_env.get_template('basic-map')
#         self.response.headers['Content-Type'] = 'html'
#         self.response.write(map_template.render())

# #possibly change /home ---> / so it's the default page?
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/fastestpath', FastPage),
    # ('/map', MapPage)
], debug=True)
