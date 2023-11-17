from sanic import Sanic
from sanic.response import redirect
from sanic_jinja2 import SanicJinja2
from model.post import Post
import uuid

app = Sanic("Hej")
app.static("/static", "./static")
jinja = SanicJinja2(app)

notes = []

logge_ind = []

globals = {"menu": {"Startside":"/", "Opret": "/opret", "Noter": "/noter"},
           "loggingon": {"Log Ind": "/logind"},
           "logge_ind": logge_ind,
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

@app.get("/logind")
@jinja.template("logind.html")
async def logind(request):
    return globals

@app.post("/Note")
async def Note(request):
    title = request.form.get('Emne')
    text = request.form.get('Note')
    id = str(uuid.uuid4())

    note = {"id": id, "title": title, "text": text}
    notes.append(note)
    return redirect("/noter")

@app.post("/login")
async def login(request):
    brugernavn = request.form.get('Navn')
    adgangskode = request.form.get('Adgangskode')
    id = str(uuid.uuid4())

    login_entry = {"id": id, "brugernavn": brugernavn, "adgangskode": adgangskode}
    logge_ind.append(login_entry)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug = True)