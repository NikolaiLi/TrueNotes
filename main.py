from sanic import Sanic
from sanic.response import redirect 
from sanic_jinja2 import SanicJinja2

app = Sanic("Hej")
app.static("/static", "./static")
jinja = SanicJinja2(app)


@app.get("/")
@jinja.template("index.html")
async def index(request):
    return None

@app.get("/noter")
@jinja.template("noter.html")
async def noter(request):
    return None

@app.get("/opret")
@jinja.template("opret.html")
async def opret(request):
    return None

@app.post("/tilnoter")
async def til_noter(request):
     return redirect("/noter")

@app.post("/tilstart")
async def til_start(request):
    return redirect("/")

@app.post("/tilopret")
async def til_opret(request):
    return redirect("/opret")

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug = True)