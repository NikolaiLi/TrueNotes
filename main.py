from sanic import Sanic
from sanic.response import redirect 
from sanic_jinja2 import SanicJinja2

app = Sanic("Hej")
app.static("/static", "./static")
jinja = SanicJinja2(app)

globals = {}


@app.get("/")
@jinja.template("index.html")
async def index(request):
    return None


@app.post("/add")
async def add_number(request):
     return redirect(f"/")

if __name__ == "__main__":
    app.run(host="localhost", port=8080)