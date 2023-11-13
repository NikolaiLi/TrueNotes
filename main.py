from sanic import Sanic
from sanic.response import redirect
from sanic_jinja2 import SanicJinja2
from model.post import Post
import uuid

app = Sanic("Hej")
app.static("/static", "./static")
jinja = SanicJinja2(app)

notes = []

globals = {"menu": {"Startside":"/", "Opret": "/opret", "Noter": "/noter"},
           "loggingon": {"Log Ind": "/logind"},
           "posts": {},
           "notes": notes
           }



@app.get("/", name = "index")
@jinja.template("index.html")
async def index(request):
    return globals

@app.get("/noter", name = "noter_page")
@jinja.template("noter.html")
async def noter(request):
    return globals

@app.get("/opret", name = "opret")
@jinja.template("opret.html")
async def opret(request):
    return globals

@app.post("/Note")
async def Note(request):
    title = request.form.get('Emne')
    text = request.form.get('Note')
    id = str(uuid.uuid4())

    note = {"id": id, "title": title, "text": text}

    notes.append(note)

    return redirect("/noter")

@app.get("/logind")
@jinja.template("logind.html")
async def logind(request):
    return globals

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug = True)