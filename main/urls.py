import tour_page
import user
from .settings import project
import home_page

tour_page.tour.add_url_rule(rule = "/tour", view_func = tour_page.render_tour, methods = ["GET", "POST"])
tour_page.tour.add_url_rule(rule = "/tour_info/<int:id>", view_func = tour_page.render_tour_info, methods = ["GET", "POST"])
project.register_blueprint(blueprint = tour_page.tour)


user.user_page.add_url_rule(rule="/user", view_func=user.render_user)
project.register_blueprint(blueprint=user.user_page)

home_page.home .add_url_rule(rule="/", view_func=home_page.render_home)
project.register_blueprint(blueprint=home_page.home)



