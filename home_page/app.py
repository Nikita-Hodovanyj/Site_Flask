import flask

home = flask.Blueprint(
    name = "home",
    import_name = "home_page",
    template_folder = "templates"
   
    
) 