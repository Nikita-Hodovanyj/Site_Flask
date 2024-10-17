import flask, pandas, os
from .models import Tour
from main.settings import DATABASE
from datetime import date

def render_tour():
  
  if True:
    path_xlsx = os.path.abspath(__file__ + "/../tours_table.xlsx")
    read_xlsx = pandas.read_excel(
      io = path_xlsx,
      header = None,
      names = ["title", "date", "country", "price", "description"]
    )
    Tour.query.delete()
    print(read_xlsx)
    for row in read_xlsx.iterrows():
        row_data = row[1]
        tour = Tour(
          title = row_data['title'],
          date = row_data['date'].date(),
          country = row_data['country'],
          price = row_data['price'],
          description = row_data['description']
        )
        DATABASE.session.add(tour)
    DATABASE.session.commit()





  return flask.render_template(template_name_or_list = "tour.html", tours = Tour.query.all())


def render_tour_info(id):
  tour_id = Tour.query.get(id)
  return flask.render_template(template_name_or_list = "tour_info.html", tour = tour_id)