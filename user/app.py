import flask

user_page = flask.Blueprint(
    name = "user_page",
    import_name ="user",
    template_folder = "templates",
    static_folder = "static",
    static_url_path = "/user"

)