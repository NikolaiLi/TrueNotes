from sanic import Sanic
from sanic.response import redirect 
from sanic_jinja2 import SanicJinja2
from model.post import Post
import uuid


app = Sanic("Blog-pages")
app.static("/static", "./static")
jinja = SanicJinja2(app)

globals ={ 
           "menu": {"Frontpage":"/", "About":"/about", "Write blog":"/write_blog", "Posts":"/posts"},
           "posts": {}
         }

@app.get("/")
@jinja.template("index.html")
async def home(request):
    return globals

if __name__ == "__main__":
    app.run(host="localhost", port=8080)