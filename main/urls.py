
import user 
import tour_page
from .settings import project

user.user_page.add_url_rule(rule="/user", view_func=user.render_user)
project.register_blueprint(blueprint=user.user_page)

tour_page.tour.add_url_rule(rule = "/tour", view_func = tour_page.render_tour)
project.register_blueprint(blueprint = tour_page.tour)

