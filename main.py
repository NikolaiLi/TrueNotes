from sanic import Sanic
from sanic.response import redirect
from sanic_jinja2 import SanicJinja2
import uuid

app = Sanic("TrueNotes")
app.static("/static", "./static")
jinja = SanicJinja2(app)

notes = []

sign_up = []

globals = {"menu": {"Oversigt":"/", "Opret": "/opret", "Noter": "/noter"},
           "loggingon": {"Log Ind": "/logind"},
           "posts": {},
           "notes": notes,
           "sign_up":{},
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

@app.get("/signup", name = "signup-page")
@jinja.template("signup.html")
async def signup(request):
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
    
    match = next((user for user in sign_up if user ["sign_up_brugernavn"] == brugernavn), None)
    
    if match and match["sign_up_adgangskode"] == adgangskode:
        redirect_obj = redirect("/")
        redirect_obj.cookies["user_id"] = match["id"]
        return redirect_obj
    else:
        return redirect("/logind")

@app.post("/signup")
async def signup(request):
    sign_up_brugernavn = request.form.get('Navn')
    sign_up_gmail = request.form.get('Gmail')
    sign_up_adgangskode = request.form.get('Adgangskode')
    id = str(uuid.uuid4())

    sign_up_entry = {"id": id, "sign_up_brugernavn": sign_up_brugernavn, "sign_up_gmail": sign_up_gmail, "sign_up_adgangskode": sign_up_adgangskode}
    sign_up.append(sign_up_entry)
    return redirect("/logind")

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug = True)