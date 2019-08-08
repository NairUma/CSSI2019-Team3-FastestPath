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
        url = "/css/images/MAPS/endstarconflict.png"
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

def timer_pick(location_one, location_two):
    if location_one == location_two:
        the_timer = "/css/images/TIMERS/"
    elif location_one == "3":
        if location_two == "4":
            the_timer = "/css/images/TIMERS/usu_to_kellogg.jpg"
        if location_two == "5":
            the_timer = "/css/images/TIMERS/kellogg_to_starbucks.jpg"
        if location_two == "1":
            the_timer = "/css/images/TIMERS/sbsb_to_kellogg.jpg"
        if location_two == "2":
            the_timer = "/css/images/TIMERS/ps1_to_kellogg.jpg"
    elif location_one == "4":
        if location_two == "3":
            the_timer = "/css/images/TIMERS/usu_to_kellogg.jpg"
        if location_two == "5":
            the_timer = "/css/images/TIMERS/usu_to_starbucks.jpg"
        if location_two == "1":
            the_timer = "/css/images/TIMERS/usu_to_sbsb.jpg"
        if location_two == "2":
            the_timer = "/css/images/TIMERS/usu_to_ps1.jpg"
    elif location_one == "5":
        if location_two == "3":
            the_timer = "/css/images/TIMERS/kellogg_to_starbucks.jpg"
        if location_two == "4":
            the_timer = "/css/images/TIMERS/usu_to_starbucks.jpg"
        if location_two == "1":
            the_timer = "/css/images/TIMERS/sbsu_to_starbucks.jpg"
        if location_two == "2":
            the_timer = "/css/images/TIMERS/ps1_to_starbucks.jpg"
    elif location_one == "1":
        if location_two == "3":
            the_timer = "/css/images/TIMERS/sbsb_to_kellogg.jpg"
        if location_two == "4":
            the_timer = "/css/images/TIMERS/usu_to_sbsb.jpg"
        if location_two == "5":
            the_timer = "/css/images/TIMERS/sbsu_to_starbucks.jpg"
        if location_two == "2":
            the_timer = "/css/images/TIMERS/ps1_to_sbsb.jpg"
    elif location_one == "2":
        if location_two == "3":
            the_timer = "/css/images/TIMERS/ps1_to_kellogg.jpg"
        if location_two == "4":
            the_timer = "/css/images/TIMERS/usu_to_ps1.jpg"
        if location_two == "5":
            the_timer = "/css/images/TIMERS/ps1_to_starbucks.jpg"
        if location_two == "1":
            the_timer = "/css/images/TIMERS/ps1_to_sbsb.jpg"
    else:
        the_timer = "/css/images/TIMERS/"
    return the_timer

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

class MapPage(webapp2.RequestHandler):
    def get(self):
        map_template = the_jinja_env.get_template('templates/map.html')
        self.response.headers['Content-Type'] = 'html'
        the_variable_dict = {
            "img_url": "/css/images/MAPS/MAPTEMPLATE.png"
        }
        self.response.write(map_template.render(the_variable_dict))

class AboutPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/about.html')
        self.response.headers['Content-Type'] = 'html'
        self.response.write(about_template.render())


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/fastestpath', FastPage),
    ('/map', MapPage),
    ('/about', AboutPage)
], debug=True)
