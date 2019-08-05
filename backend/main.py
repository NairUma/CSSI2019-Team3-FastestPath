import webapp2
import jinja2
import os


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# this the home page, using /home
class MainPage(webapp2.RequestHandler):
    def get(self):
        main_template = the_jinja_env.get_template('CSSI2019-Team3-FastestPath/frontend/index1.html')
        self.response.headers['Content-Type'] = 'html'
        self.response.write('This is our main page')
# this the map page, using /fastestpath
class FastPage(webapp2.RequestHandler):
    def get(self):
        # insert html title where *** is
        results_template = the_jinja_env.get_template('***')
        the_variable_dict = {
            "startpoint": "[insert location]",
            "endpoint": "[insert destination]",
            "img_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVGEpAnhFQoTdolA3y8j0vPqYtt2JtyGKSVT5vsGkh8nFiHPsa"
        }
        self.response.write(results_template.render(the_variable_dict))

    def post(self):
        results_template = the_jinja_env.get_template('templates/results.html')
        location_one = self.request.get('user_loc1')
        location_two = self.request.get('user_loc2')
        correct_map = self.request.get('map')

        pic_url = get_meme_url(meme_img_choice)
        the_variable_dict = {"startpoint": user_loc1,
                             "endpoint": user_loc2S,
                             "img_url": pic_url}
        self.response.write(results_template.render(the_variable_dict))

app = webapp2.WSGIApplication([
    ('/home', MainPage),
    ('/fastestpath', FastPage)
], debug=True)
