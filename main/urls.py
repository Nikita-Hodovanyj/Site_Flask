import tour_page
from .settings import project

tour_page.tour.add_url_rule(rule = "/tour", view_func = tour_page.render_tour)
project.register_blueprint(blueprint = tour_page.tour)

