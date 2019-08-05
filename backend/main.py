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
        self.response.headers['Content-Type'] = 'html'
        self.response.write('This is our main page')
# this the map page, using /fastestpath
class FastPage(webapp2.RequestHandler):
    def get(self):
        # insert html title where *** is
        results_template = the_jinja_env.get_template('***')
        the_variable_dict = {
            "startspoint": "If Cinderella's shoe was a perfect fit",
            "line2": "Why did it fall off?",
            "img_url": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Deep_in_thought.jpg"
        }
        self.response.write(results_template.render(the_variable_dict))

    def post(self):
        results_template = the_jinja_env.get_template('templates/results.html')
        meme_first_line = self.request.get('user-first-ln')
        meme_second_line = self.request.get('user-second-ln')
        meme_img_choice = self.request.get('meme-type')

        pic_url = get_meme_url(meme_img_choice)
        the_variable_dict = {"line1": meme_first_line,
                             "line2": meme_second_line,
                             "img_url": pic_url}
        self.response.write(results_template.render(the_variable_dict))

app = webapp2.WSGIApplication([
    ('/home', MainPage),
    ('/fastestpath', FastPage)
], debug=True)
