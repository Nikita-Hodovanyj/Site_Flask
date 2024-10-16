import tour_page
from .settings import project

tour_page.tour.add_url_rule(rule = "/tour", view_func = tour_page.render_tour, methods = ["GET", "POST"])
tour_page.tour.add_url_rule(rule = "/tour_info/<int:id>", view_func = tour_page.render_tour_info, methods = ["GET", "POST"])

project.register_blueprint(blueprint = tour_page.tour)


