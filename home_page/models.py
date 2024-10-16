from main.settings import DB

class Data(DB.Model):
    id = DB.Column(DB.Integer, primary_key = True)
    name = DB.Column(DB.String(30), nullable = False)
    email = DB.Column(DB.String(40), nullable = False)
    review = DB.Column(DB.String, nullable = False)

    def __repr__(self):
      return f"id користувача - {self.id}; Email користувача {self.email}; Review користувача {self.review};"