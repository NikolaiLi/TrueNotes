from sanic import Sanic
from sanic.response import redirect 
from sanic_jinja2 import SanicJinja2
from model.post import Post
import uuid

app = Sanic("Hej")
app.static("/static", "./static")
jinja = SanicJinja2(app)

globals = {"menu": {"Startside":"/", "Opret": "/opret", "Noter": "/noter", "Log Ind": "/logind"},
           "posts": {}
           }

@app.get("/")
@jinja.template("index.html")
async def index(request):
    return globals

@app.get("/noter")
@jinja.template("noter.html")
async def noter(request):
    return globals

@app.get("/opret")
@jinja.template("opret.html")
async def opret(request):
    return globals

@app.get("/logind")
@jinja.template("logind.html")
async def logind(request):
    return globals

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug = True)