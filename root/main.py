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
        url = "/css/images/MAPS/endstartconflict.png"
    elif location_one == "3":
        if location_two == "4":
            url = "/css/images/MAPS/4-3.png"
        if location_two == "5":
            url = "/css/images/MAPS/3-5.png"
        if location_two == "1":
            url = "/css/images/MAPS/1-3.png"
        if location_two == "2":
            url = "/css/images/MAPS/2-3.png"
    elif location_one == "4":
        if location_two == "3":
            url = "/css/images/MAPS/4-3.png"
        if location_two == "5":
            url = "/css/images/MAPS/4-5.png"
        if location_two == "1":
            url = "/css/images/MAPS/1-4.png"
        if location_two == "2":
            url = "/css/images/MAPS/2-4.png"
    elif location_one == "5":
        if location_two == "3":
            url = "/css/images/MAPS/3-5.png"
        if location_two == "4":
            url = "/css/images/MAPS/4-5.png"
        if location_two == "1":
            url = "/css/images/MAPS/1-5.png"
        if location_two == "2":
            url = "/css/images/MAPS/2-5.png"
    elif location_one == "1":
        if location_two == "3":
            url = "/css/images/MAPS/1-3.png"
        if location_two == "4":
            url = "/css/images/MAPS/1-4.png"
        if location_two == "5":
            url = "/css/images/MAPS/1-5.png"
        if location_two == "2":
            url = "/css/images/MAPS/2-3.png"
    elif location_one == "2":
        if location_two == "3":
            url = "/css/images/MAPS/2-3.png"
        if location_two == "4":
            url = "/css/images/MAPS/2-4.png"
        if location_two == "5":
            url = "/css/images/MAPS/2-5.png"
        if location_two == "1":
            url = "/css/images/MAPS/2-1.png"
    else:
        url = "/css/images/MAPS/locerroruse.png"
    return url

# # this the home page, using /home
class MainPage(webapp2.RequestHandler):
    def get(self):
        main_template = the_jinja_env.get_template('templates/index.html')
        self.response.headers['Content-Type'] = 'html'

        self.response.write(main_template.render())

    def post(self):
        pass

# # this the map page, using /fastestpath
class FastPage(webapp2.RequestHandler):
    def get(self):
        end_template = the_jinja_env.get_template('templates/map.html')
        # adding request.get *********************************

        start_choice = self.request.get('start')
        dest_choice = self.request.get('dest')
        map_url = map_pick(start_choice, dest_choice)
        the_variable_dict = {
            "start": start_choice,
            "dest": dest_choice,
            "img_url": map_url
        }
        self.response.write(end_template.render(the_variable_dict))

    def post(self):
        # results_template = the_jinja_env.get_template('templates/map.html')
        # location_one = self.request.get('starting point')
        # location_two = self.request.get('destination')
        # map_url = map_pick(location_one, location_two)
        # the_variable_dict = {
        #     "img_url": "map_url"
        # }
        # self.response.write(results_template.render(the_variable_dict))
        pass

# class MapPage(webapp2.RequestHandler):
#     def get(self):
#         map_template = the_jinja_env.get_template('basic-map')
#         self.response.headers['Content-Type'] = 'html'
#         self.response.write(map_template.render())

# #possibly change /home ---> / so it's the default page?
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/fastestpath', FastPage)
    # ('/map', MapPage)
], debug=True)
