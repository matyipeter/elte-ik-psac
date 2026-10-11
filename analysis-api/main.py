import json
import random
from http.server import BaseHTTPRequestHandler, HTTPServer

questions = [
    "Definiálja a metrikus tér fogalmát!",
    "Adja meg a normált tér fogalmát!",
    "Mit nevezünk norma által indukált metrikának?",
    "Adjon meg három különböző normát az R^n lineáris téren!",
    "Mikor mondjuk, hogy egy sorozat konvergens az (X, ||·||) normált térben?",
    "Definiálja a normált térbeli sorozatok konvergenciájának a fogalmát!",
    "Milyen kapcsolat van egy R^n-beli sorozat konvergenciája és a koordinátasorozatainak konvergenciája között?",
    "Legyen (X, ||·||) normált tér, és A ⊂ X. Mikor mondjuk, hogy az a ∈ X pont torlódási pontja az A halmaznak?",
    "Legyen (X, ||·||) normált tér és A ⊂ X. Mikor mondjuk, hogy az a ∈ X pont belső pontja az A halmaznak?",
    "Definiálja a nyílt halmaz fogalmát normált térben!",
    "Definiálja a zárt halmaz fogalmát normált térben!",
    "Jellemezze a zárt halmazokat a torlódási pont segítségével!",
    "Jellemezze a zárt halmazokat a konvergens sorozatok segítségével!",
    "Legyen X lineáris tér, és ||·||_1, ||·||_2 két norma az X téren. Mikor mondjuk, hogy ez a két norma ekvivalens?",
    "Definiálja az euklideszi tér fogalmát!",
    "Mit nevezünk a skaláris szorzat által indukált normának?",
    "Mit állít a Cauchy–Schwarz-egyenlőtlenség?",
    "Mit tud mondani az R^n-beli (n ∈ N, n ≥ 1) normák ekvivalenciájáról?",
    "Mikor mondjuk, hogy egy normált tér teljes?",
    "Adjon példát nem teljes normált térre!",
    "Mit állít a Cauchy-féle konvergenciakritérium az R^n euklideszi térbeli sorozatokra?",
    "Mit állít a Bolzano–Weierstrass-féle kiválasztási tétel az R^n euklideszi térre?",
    "Mikor mondjuk, hogy egy f: R^n -> R^m függvény folytonos egy adott pontban?",
    "Definiálja a folytonosság fogalmát normált terek közötti függvényekre!",
    "Mit mond a folytonosságra vonatkozó átviteli elv normált terek közötti függvények esetére?",
    "Definiálja az R^n (n ∈ N, n ≥ 1) téren értelmezett projekciófüggvényeket!",
    "Mondja ki az összetett függvény folytonosságára vonatkozó tételt többváltozós függvények esetére!",
    "Milyen kapcsolat van egy függvény folytonossága és a koordinátafüggvényei folytonossága között?",
    "Fogalmazza meg a Weierstrass-tételt többváltozós függvények esetére!",
    "Mik a kompakt halmazok az R^n (n ∈ N, n ≥ 1) térben?",
    "Definiálja a határérték fogalmát normált terek közötti függvényekre!",
    "Mikor mondjuk, hogy egy f: R^n -> R^m függvénynek van pontbeli határértéke?",
    "Mit mond a határértékre vonatkozó átviteli elv R^n -> R^m típusú függvények esetére?",
    "Adja meg egy R^n -> R (n ∈ N, n ≥ 1) típusú függvény pontbeli i-edik változó szerinti parciális deriváltjának fogalmát!",
    "Adja meg egy R^n -> R (n ∈ N, n ≥ 1) típusú függvény pontbeli v irányú iránymenti deriváltjának fogalmát!",
    "Hogyan számítható ki egy iránymenti derivált a parciális deriváltak ismeretében? Adja meg az ehhez elegendő feltételeket!",
    "Adja meg a totális derivált fogalmát!",
    "Hogyan fogalmazható át a totális deriválhatóság lineáris közelítéssel?",
    "Milyen kapcsolat van a totális derivált és a folytonosság között?",
    "Adjon példát olyan R^n -> R típusú függvényre, amely folytonos, de nem totálisan differenciálható egy adott pontban!",
    "Milyen kapcsolat van a totális és az iránymenti derivált között?",
    "Adja meg a Jacobi-mátrix fogalmát!",
    "Mit állít a deriváltmátrix előállításáról szóló tétel?",
    "Milyen feltételek mellett következik a parciális deriválhatóságból a totális deriválhatóság?",
    "Adja meg az érintősík fogalmát!",
    "Mit mond az összetett függvény deriválási szabálya többváltozós függvények esetén?",
    "Adja meg a gradiens vektor fogalmát!",
    "Legyen f: R^n -> R és f ∈ D{a}. Milyen v ∈ R^n irányban lesz a ∂_v f(a) iránymenti derivált értéke a legnagyobb?",
    "Legyen f: R^n -> R és f ∈ D{a}. Milyen v ∈ R^n irányban lesz a ∂_v f(a) iránymenti derivált értéke nulla?",
    "Mikor mondjuk, hogy az f: R^n -> R függvény kétszer differenciálható az a ∈ int(Df) pontban?",
    "Mikor mondjuk, hogy az f: R^n -> R függvény kétszer folytonosan differenciálható az a ∈ int(Df) pontban?",
    "Adja meg a Hesse-féle mátrix fogalmát!",
    "Mondja ki a Young-tételt!",
    "Mit állít a 'Taylor-formula a Lagrange-féle maradéktaggal' című tétel?",
]


def pick_random_questions(q_list, count=5):
    # random.sample ismétlés nélküli mintavételezést végez
    selected = random.sample(q_list, count)
    return selected

class QuestionHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/questions":
            try:
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                data = pick_random_questions(questions)
                self.wfile.write(json.dumps(data).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), QuestionHandler)
    print("Serving on port 8000...")
    server.serve_forever()
