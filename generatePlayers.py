##########################
# Code generates the game Database including players,teams and their various features.
########################
########################
#MatchSetup.py
#Lines 10-397: Team and Player Data adapted from Football Manger 19 by SEGAgames
#            : Images gotten from google Images(various sources)
#Linese 404-End: Original code
########################
from player_Design import*

def getTeams():
    t1=Team("Borussia Dortmund",[(201, 204, 24),(10,10,10),(232, 235, 239)],"BVB",[4,4,2],"bvb.png")
    t2=Team("Atletico Madrid",[(198, 37, 59),(89, 186, 191),(60, 84, 112)],"ATL",[4,4,2],"atl.png")
    t3=Team("Club Brugge",[(79, 118, 165),(255, 252, 252),(198, 37, 59)],"FCB",[4,3,3],"brugge.png")
    t4=Team("AS Monaco",[(198, 37, 59),(85, 109, 83),(184, 232, 242)],"ASM",[4,4,2],"monaco.png")
    t5=Team("Barcelona",[(15, 53, 99),(213, 239, 214),(249, 224, 239)],"BAR",[4,3,3],"barca.png")
    t6=Team("Inter Milan",[(15, 53, 99),(255, 252, 252),(232, 235, 239)],"INT",[4,3,3],"inter.png")
    t7=Team("Tottenham Hotspurs",[(255, 252, 252),(63, 122, 193),(18, 188, 134)],"TOT",[4,3,3],"spurs.png")
    t8=Team("PSV Eindhoven",[(198, 37, 59),(255, 252, 252),(60, 84, 112)],"PSV",[4,3,3],"psv.jpg")
    t9=Team("Napoli",[(79, 118, 165),(10,10,10),(181, 186, 191)],"NAP",[4,3,3],"napoli.png")
    t10=Team("Liverpool",[(198, 37, 59),(104, 14, 140),(181, 186, 191)],"LIV",[4,3,3],"liverpool.png")
    t11=Team("Paris Saint Germain",[(15, 53, 99),(10,10,10),(255, 252, 252)],"PSG",[4,2,4],"psg.png")
    t12=Team("Red Star Belgrade",[(10,10,10),(15, 53, 99),(198, 37, 59)],"RSB",[4,3,3],"rsb.jpg")
    t13=Team("Porto FC",[(79, 118, 165),(232, 235, 239),(15, 53, 99)],"FCP",[4,4,2],"fcp.jpg")
    t14=Team("Schalke 04",[(79, 118, 165),(232, 235, 239),(90, 239, 52)],"SCH",[3,5,2],"schalke.png")
    t15=Team("Galatasary",[(239, 164, 51),(10,10,10),(255, 252, 252)],"GAL",[4,3,3],"gal.jpg")
    t16=Team("Lokomotiv Moscow",[(198, 37, 59),(255, 252, 252),(104, 14, 140)],"LOK",[4,3,3],"lok.jpg")
    t17=Team("Bayern Munich",[(198, 37, 59),(184, 239, 227),(255, 252, 252)],"BAY",[4,2,4],"bay.jpg")
    t18=Team("Ajax",[(198, 37, 59),(10,10,10),(255, 252, 252)],"AJA",[4,3,3],"ajax.jpg")
    t19=Team("Benfica",[(198, 37, 59),(255, 252, 252),(10,10,10)],"BEN",[4,3,3],"benfica.png")
    t20=Team("AEK Athens",[(201, 204, 24),(10,10,10),(79, 118, 165)],"AEK",[4,4,2],"aek.png")
    t21=Team("Manchester City",[(184, 232, 242),(60, 84, 112),(104, 14, 140)],"MCI",[4,3,3],"man city.jpg")
    t22=Team("Shaktar Donetsk",[(234, 152, 58),(232, 235, 239),(10,10,10)],"SHAKT",[4,3,3],"shaktar.jpeg")
    t23=Team("Olyimpque Lyon",[ (255, 252, 252),(232, 235, 239),(234, 152, 58)],"OL",[4,3,3],"ol.jpg")
    t24=Team("Hoffenheim",[(79, 118, 165),(10,10,10),(71, 63, 44)],"HOF",[5,3,2],"hoff.jpg")
    t25=Team("Real Madrid",[(255, 252, 252),(10,10,10),(198, 37, 59)],"RMD",[4,3,3],"real.jpg")
    t26=Team("AS Roma",[(71, 63, 44),(232, 235, 239),(201, 183, 24)],"ASR",[4,3,3],"roma.png")
    t27=Team("Pizen",[(198, 37, 59),(255, 252, 252),(234, 152, 58)],"PIZ",[4,3,3],"pizen.jpg")
    t28=Team("CSKA Moscow",[(198, 37, 59),(79, 118, 165),(234, 152, 58)],"CSKA",[5,3,2],"cska.jpg")
    t29=Team("Juventus",[(255, 252, 252),(10,10,10),(7, 32, 61)],"JUV",[4,4,2],"juve.jpg")
    t30=Team("Manchester United",[(198, 37, 59),(229, 211, 232),(7, 32, 61)],"MUN",[4,3,3],"man utd.png")
    t31=Team("Valencia",[(255, 252, 252),(15, 53, 99),(234, 152, 58)],"VAL",[4,4,2],"valencia.jpg")
    t32=Team("Young Boys",[(201, 204, 24),(89, 186, 191),(255, 252, 252)],"YOB",[4,4,2],"yob.png")
    return [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,
    t21,t22,t23,t4,t25,t26,t27,t28,t29,t30,t31,t32]

def getPlayers():
    return [
    Defender("Akanji",16,[5,16,14,6,10],"Borussia Dortmund"),
    Defender("Gurrero",13,[14,13,14,14,11],"Borussia Dortmund"),
    Defender("Toprak",36, [4,14,15,11,8],"Borussia Dortmund"),
    Defender("Toljan",15, [10,11,16,13,15],"Borussia Dortmund"),
    Midfielder("Witsel",28,[12,13,13,15,11],"Borussia Dortmund"),
    Midfielder("Delaney",6,[11,14,11,10,18],"Borussia Dortmund"),
    Midfielder("Gotze",10,[13,7,11,18,10],"Borussia Dortmund"),
    Forward("Reus",11,[16,6,17,15,14],"Borussia Dortmund"),
    Forward("Sancho",7,[13,5,16,14,9],"Borussia Dortmund"),
    Forward("Alcacer",9,[15,7,14,13,15],"Borussia Dortmund"),
    Goalie("Burki",1,[15,12],"Borussia Dortmund"),
    Defender("Godin",3,[4,18,12,9,14],"Atletico Madrid"),
    Defender("Vrsaljko",16,[13,14,13,12,15],"Atletico Madrid"),
    Defender("Savic",15,[7,15,12,11,13],"Atletico Madrid"),
    Defender("Luis",3, [13,12,11,16,13],"Atletico Madrid"),
    Midfielder("Saul",8,[13,13,13,16,8],"Atletico Madrid"),
    Midfielder("Koke",6,[13,13,13,15,14],"Atletico Madrid"),
    Midfielder("Lemar",11,[16,6,17,17,7],"Atletico Madrid"),
    Midfielder("Correa",10,[15,5,14,17,10],"Atletico Madrid"),
    Forward("Griezmann",7,[17,6,15,17,13],"Atletico Madrid"),
    Forward("Costa",9,[14,8,14,13,20],"Atletico Madrid"),
    Goalie("Oblak",1,[17,17],"Atletico Madrid"),
    Goalie("Oblak",1,[17,17],"Club Brugge"),
    Defender("Oblak",10,[15,5,14,17,10],"Club Brugge"),
    Defender("Oblak",10,[15,5,14,17,10],"Club Brugge"),
    Defender("Oblak",10,[15,5,14,17,10],"Club Brugge"),
    Defender("Oblak",10,[15,5,14,17,10],"Club Brugge"),
    Midfielder("Oblak",10,[15,5,14,17,10],"Club Brugge"),
    Midfielder("Oblak",10,[15,5,14,17,10],"Club Brugge"),
    Midfielder("Oblak",10,[15,5,14,17,10],"Club Brugge"),
    Forward("Oblak",10,[15,5,14,17,10],"Club Brugge"),
    Forward("Oblak",10,[15,5,14,17,10],"Club Brugge"),
    Forward("Oblak",10,[15,5,14,17,10],"Club Brugge"),
    Goalie("Subasic",1,[15,13],"AS Monaco"),
    Defender("Sidibe",19,[13,14,13,14,13],"AS Monaco"),
    Defender("Jorge",5,[5,15,14,12,14],"AS Monaco"),
    Defender("Gilk",25,[4,17,10,10,17],"AS Monaco"),
    Defender("Jorge",3,[13,14,14,15,12],"AS Monaco"),
    Midfielder("Golovin",17,[14,10,13,15,8],"AS Monaco"),
    Midfielder("Lopes",7,[14,4,15,15,10],"AS Monaco"),
    Midfielder("Tielemans",8,[12,10,13,16,11],"AS Monaco"),
    Midfielder("Jovetic",10,[15,5,12,15,10],"AS Monaco"),
    Forward("Falcao",9,[15,5,14,17,10],"AS Monaco"),
    Forward("Keita",11,[14,2,16,15,11],"AS Monaco"),

    Goalie("Handandovic",1,[18,10],"Inter Milan"),
    Defender("Ansladi",3,[13,14,13,13,15],"Inter Milan"),
    Defender("Skrinar",37,[6,17,13,11,13],"Inter Milan"),
    Defender("De Vrij",6,[7,17,12,12,16],"Inter Milan"),
    Defender("Asamoah",18,[12,14,14,14,14],"Inter Milan"),
    Midfielder("Vecino",10,[12,14,14,14,13],"Inter Milan"),
    Midfielder("Nainngolan",14,[13,16,15,14,18],"Inter Milan"),
    Midfielder("Brozovic",77,[13,12,13,16,10],"Inter Milan"),
    Forward("Perisic",44,[14,7,16,14,8],"Inter Milan"),
    Forward("Icardi",9,[17,5,14,14,8],"Inter Milan"),
    Forward("Candreva",87,[15,6,14,16,10],"Inter Milan"),

    Goalie("Lloris",1,[17,10],"Tottenham Hotspurs"),
    Defender("Rose",3,[12,15,15,13,16],"Tottenham Hotspurs"),
    Defender("Vertonghen",5,[11,16,12,15,14],"Tottenham Hotspurs"),
    Defender("Alderwield",4,[10,15,13,13,13],"Tottenham Hotspurs"),
    Defender("Trippier",2,[13,14,14,13,12],"Tottenham Hotspurs"),
    Midfielder("Dembele",19,[14,15,14,17,12],"Tottenham Hotspurs"),
    Midfielder("Dier",15,[12,15,12,12,15],"Tottenham Hotspurs"),
    Midfielder("Eriksen",23,[16,8,12,17,5],"Tottenham Hotspurs"),
    Forward("Son Heung-Min",7,[14,6,15,15,8],"Tottenham Hotspurs"),
    Forward("Kane",10,[18,10,13,15,11],"Tottenham Hotspurs"),
    Forward("Alli",20,[15,10,11,16,12],"Tottenham Hotspurs"),

    Goalie("Zoet",1,[15,11],"PSV Eindhoven"),
    Defender("Viergever",4,[10,14,11,11,11],"PSV Eindhoven"),
    Defender("Dumfries",22,[13,11,13,12,12],"PSV Eindhoven"),
    Defender("Hendrix",8,[11,13,11,13,10],"PSV Eindhoven"),
    Defender("Isimat-Marin",2,[7,13,15,11,12],"PSV Eindhoven"),
    Midfielder("Thomas",30,[12,6,13,14,10],"PSV Eindhoven"),
    Midfielder("Gutierrez",25,[11,12,12,14,8],"PSV Eindhoven"),
    Midfielder("Bergwijn",17,[13,5,13,12,3],"PSV Eindhoven"),
    Forward("Lozano",11,[14,5,15,15,6],"PSV Eindhoven"),
    Forward("De Jong",9,[15,5,14,17,10],"PSV Eindhoven"),
    Forward("Romero",10,[12,4,11,13,12],"PSV Eindhoven"),

    Goalie("Ospina",1,[17,17],"Napoli"),
    Defender("Albiol",33,[10,14,11,12,13],"Napoli"),
    Defender("Koulibaly",26,[6,17,15,12,15],"Napoli"),
    Defender("Hysaj",23,[11,14,15,12,15],"Napoli"),
    Defender("Ghoulam",31,[15,5,14,17,10],"Napoli"),
    Midfielder("Allan",5,[13,15,13,14,16],"Napoli"),
    Midfielder("Hamsik",10,[15,9,15,16,11],"Napoli"),
    Midfielder("Zielenski",20,[13,10,14,17,11],"Napoli"),
    Forward("Mertens",10,[16,5,16,16,12],"Napoli"),
    Forward("Isigne",10,[17,6,15,17,10],"Napoli"),
    Forward("Callejon",10,[14,8,15,16,12],"Napoli"),

    Goalie("Alisson",1,[17,17],"Liverpool"),
    Defender("Robertson",26,[14,14,15,14,13],"Liverpool"),
    Defender("Van Dijk",4,[5,14,14,13,17],"Liverpool"),
    Defender("Gomez",12,[11,14,15,13,10],"Liverpool"),
    Defender("Arnold",66,[14,12,14,14,14],"Liverpool"),
    Midfielder("Milner",7,[13,13,12,13,14],"Liverpool"),
    Midfielder("Henderson",14,[12,14,13,15,15],"Liverpool"),
    Midfielder("Keita",8,[15,12,14,16,17],"Liverpool"),
    Forward("Mane",10,[16,9,18,16,10],"Liverpool"),
    Forward("Firmino",9,[16,13,18,14,13],"Liverpool"),
    Forward("Salah",11,[17,8,18,16,9],"Liverpool"),

    Goalie("Buffon",1,[18,10],"Paris Saint Germain"),
    Defender("Kurzawa",20,[13,11,15,14,10],"Paris Saint Germain"),
    Defender("Marquinhos",5,[10,16,14,14,14],"Paris Saint Germain"),
    Defender("Thiago Silva",2,[6,17,12,14,17],"Paris Saint Germain"),
    Defender("Meunier",12,[13,13,12,14,10],"Paris Saint Germain"),
    Midfielder("Verrati",6,[15,10,13,17,14],"Paris Saint Germain"),
    Midfielder("Rabiot",25,[13,12,12,14,12],"Paris Saint Germain"),
    Forward("Neymar",10,[19,3,18,20,10],"Paris Saint Germain"),
    Forward("Cavani",9,[17,8,16,14,14],"Paris Saint Germain"),
    Forward("Mbappe",7,[18,2,18,20,7],"Paris Saint Germain"),
    Forward("Di Maria",11,[17,6,16,16,11],"Paris Saint Germain"),

    Goalie("Ter Stegen",1,[17,17],"Barcelona"),
    Defender("Alba",18,[14,12,17,15,15],"Barcelona"),
    Defender("Umtiti",23,[7,16,14,14,14],"Barcelona"),
    Defender("Pique",3,[10,16,11,16,14],"Barcelona"),
    Defender("Roberto",20,[13,12,15,15,11],"Barcelona"),
    Midfielder("Arthur",8,[14,12,13,14,9],"Barcelona"),
    Midfielder("Bosquets",5,[8,17,15,11,12],"Barcelona"),
    Midfielder("Rackitic",4,[16,10,13,16,11],"Barcelona"),
    Forward("Coutinho",14,[17,9,14,18,11],"Barcelona"),
    Forward("Suarez",9,[19,9,15,17,17],"Barcelona"),
    Forward("Messi",10,[20,6,14,20,11],"Barcelona"),

    Goalie("Ter Stegen",1,[17,17],"Red Star Belgrade"),
    Defender("Alba",18,[14,12,17,15,15],"Red Star Belgrade"),
    Defender("Umtiti",23,[7,16,14,14,14],"Red Star Belgrade"),
    Defender("Pique",3,[10,16,11,16,14],"Red Star Belgrade"),
    Defender("Roberto",20,[13,12,15,15,11],"Red Star Belgrade"),
    Midfielder("Arthur",8,[14,12,13,14,9],"Red Star Belgrade"),
    Midfielder("Bosquets",5,[8,17,15,11,12],"Red Star Belgrade"),
    Midfielder("Rackitic",4,[16,10,13,16,11],"Red Star Belgrade"),
    Forward("Coutinho",14,[17,9,14,18,11],"Red Star Belgrade"),
    Forward("Suarez",9,[19,9,15,17,17],"Red Star Belgrade"),
    Forward("Messi",10,[20,6,14,20,11],"Red Star Belgrade"),

    Goalie("Ter Stegen",1,[17,17],"Porto FC"),
    Defender("Alba",18,[14,12,17,15,15],"Porto FC"),
    Defender("Umtiti",23,[7,16,14,14,14],"Porto FC"),
    Defender("Pique",3,[10,16,11,16,14],"Porto FC"),
    Defender("Roberto",20,[13,12,15,15,11],"Porto FC"),
    Midfielder("Arthur",8,[14,12,13,14,9],"Porto FC"),
    Midfielder("Bosquets",5,[8,17,15,11,12],"Porto FC"),
    Midfielder("Rackitic",4,[16,10,13,16,11],"Porto FC"),
    Forward("Coutinho",14,[17,9,14,18,11],"Porto FC"),
    Forward("Suarez",9,[19,9,15,17,17],"Porto FC"),
    Forward("Messi",10,[20,6,14,20,11],"Porto FC"),

    Goalie("Neur",1,[17,17],"Bayern Munich"),
    Defender("Alaba",18,[14,12,17,15,15],"Bayern Munich"),
    Defender("Hummels",23,[7,16,14,14,14],"Bayern Munich"),
    Defender("Boateng",3,[10,16,11,16,14],"Bayern Munich"),
    Defender("Kimmich",20,[13,12,15,15,11],"Bayern Munich"),
    Midfielder("Thiago Alcantara",8,[14,12,13,14,9],"Bayern Munich"),
    Midfielder("Muller",5,[8,17,15,11,12],"Bayern Munich"),
    Midfielder("Goretzka",4,[16,10,13,16,11],"Bayern Munich"),
    Forward("Ribery",14,[17,9,14,18,11],"Bayern Munich"),
    Forward("Lewandowski",9,[19,9,15,17,17],"Bayern Munich"),
    Forward("Robben",10,[20,6,14,20,11],"Bayern Munich"),

    Goalie("Ter Stegen",1,[17,17],"Galatasary"),
    Defender("Alba",18,[14,12,17,15,15],"Galatasary"),
    Defender("Umtiti",23,[7,16,14,14,14],"Galatasary"),
    Defender("Pique",3,[10,16,11,16,14],"Galatasary"),
    Defender("Roberto",20,[13,12,15,15,11],"Galatasary"),
    Midfielder("Arthur",8,[14,12,13,14,9],"Galatasary"),
    Midfielder("Bosquets",5,[8,17,15,11,12],"Galatasary"),
    Midfielder("Rackitic",4,[16,10,13,16,11],"Galatasary"),
    Forward("Coutinho",14,[17,9,14,18,11],"Galatasary"),
    Forward("Suarez",9,[19,9,15,17,17],"Galatasary"),
    Forward("Messi",10,[20,6,14,20,11],"Galatasary"),

    Goalie("Ter Stegen",1,[17,17],"Schalke 04"),
    Defender("Alba",18,[14,12,17,15,15],"Schalke 04"),
    Defender("Umtiti",23,[7,16,14,14,14],"Schalke 04"),
    Defender("Pique",3,[10,16,11,16,14],"Schalke 04"),
    Defender("Roberto",20,[13,12,15,15,11],"Schalke 04"),
    Midfielder("Arthur",8,[14,12,13,14,9],"Schalke 04"),
    Midfielder("Bosquets",5,[8,17,15,11,12],"Schalke 04"),
    Midfielder("Rackitic",4,[16,10,13,16,11],"Schalke 04"),
    Forward("Coutinho",14,[17,9,14,18,11],"Schalke 04"),
    Forward("Suarez",9,[19,9,15,17,17],"Schalke 04"),
    Forward("Messi",10,[20,6,14,20,11],"Schalke 04"),

    Goalie("Ter Stegen",1,[17,17],"Ajax"),
    Defender("Alba",18,[14,12,17,15,15],"Ajax"),
    Defender("Umtiti",23,[7,16,14,14,14],"Ajax"),
    Defender("Pique",3,[10,16,11,16,14],"Ajax"),
    Defender("Roberto",20,[13,12,15,15,11],"Ajax"),
    Midfielder("Arthur",8,[14,12,13,14,9],"Ajax"),
    Midfielder("Bosquets",5,[8,17,15,11,12],"Ajax"),
    Midfielder("Rackitic",4,[16,10,13,16,11],"Ajax"),
    Forward("Coutinho",14,[17,9,14,18,11],"Ajax"),
    Forward("Suarez",9,[19,9,15,17,17],"Ajax"),
    Forward("Messi",10,[20,6,14,20,11],"Ajax"),

    Goalie("Ter Stegen",1,[17,17],"Benfica"),
    Defender("Alba",18,[14,12,17,15,15],"Benfica"),
    Defender("Umtiti",23,[7,16,14,14,14],"Benfica"),
    Defender("Pique",3,[10,16,11,16,14],"Benfica"),
    Defender("Roberto",20,[13,12,15,15,11],"Benfica"),
    Midfielder("Arthur",8,[14,12,13,14,9],"Benfica"),
    Midfielder("Bosquets",5,[8,17,15,11,12],"Benfica"),
    Midfielder("Rackitic",4,[16,10,13,16,11],"Benfica"),
    Forward("Coutinho",14,[17,9,14,18,11],"Benfica"),
    Forward("Suarez",9,[19,9,15,17,17],"Benfica"),
    Forward("Messi",10,[20,6,14,20,11],"Benfica"),

    Goalie("Ter Stegen",1,[17,17],"AEK Athens"),
    Defender("Alba",18,[14,12,17,15,15],"AEK Athens"),
    Defender("Umtiti",23,[7,16,14,14,14],"AEK Athens"),
    Defender("Pique",3,[10,16,11,16,14],"AEK Athens"),
    Defender("Roberto",20,[13,12,15,15,11],"AEK Athens"),
    Midfielder("Arthur",8,[14,12,13,14,9],"AEK Athens"),
    Midfielder("Bosquets",5,[8,17,15,11,12],"AEK Athens"),
    Midfielder("Rackitic",4,[16,10,13,16,11],"AEK Athens"),
    Forward("Coutinho",14,[17,9,14,18,11],"AEK Athens"),
    Forward("Suarez",9,[19,9,15,17,17],"AEK Athens"),
    Forward("Messi",10,[20,6,14,20,11],"AEK Athens"),

    Goalie("Ederson",1,[17,17],"Manchester City"),
    Defender("Mendy",23,[14,12,17,15,15],"Manchester City"),
    Defender("Laporte",14,[7,16,14,14,14],"Manchester City"),
    Defender("Stones",5,[10,16,11,16,14],"Manchester City"),
    Defender("Walker",2,[13,12,15,15,11],"Manchester City"),
    Midfielder("Silva",8,[14,12,13,14,9],"Manchester City"),
    Midfielder("Fernandinho",5,[8,17,15,11,12],"Manchester City"),
    Midfielder("De Bruyne",17,[16,10,13,16,11],"Manchester City"),
    Forward("Sterling",7,[17,9,14,18,11],"Manchester City"),
    Forward("Kun Aguero",10,[19,9,15,17,17],"Manchester City"),
    Forward("Marhez",26,[20,6,14,20,11],"Manchester City"),

    Goalie("Ter Stegen",1,[17,17],"Shaktar Donetsk"),
    Defender("Alba",18,[14,12,17,15,15],"Shaktar Donetsk"),
    Defender("Umtiti",23,[7,16,14,14,14],"Shaktar Donetsk"),
    Defender("Pique",3,[10,16,11,16,14],"Shaktar Donetsk"),
    Defender("Roberto",20,[13,12,15,15,11],"Shaktar Donetsk"),
    Midfielder("Arthur",8,[14,12,13,14,9],"Shaktar Donetsk"),
    Midfielder("Bosquets",5,[8,17,15,11,12],"Shaktar Donetsk"),
    Midfielder("Rackitic",4,[16,10,13,16,11],"Shaktar Donetsk"),
    Forward("Coutinho",14,[17,9,14,18,11],"Shaktar Donetsk"),
    Forward("Suarez",9,[19,9,15,17,17],"Shaktar Donetsk"),
    Forward("Messi",10,[20,6,14,20,11],"Shaktar Donetsk"),

    Goalie("Ter Stegen",1,[17,17],"Olyimpque Lyon"),
    Defender("Alba",18,[14,12,17,15,15],"Olyimpque Lyon"),
    Defender("Umtiti",23,[7,16,14,14,14],"Olyimpque Lyon"),
    Defender("Pique",3,[10,16,11,16,14],"Olyimpque Lyon"),
    Defender("Roberto",20,[13,12,15,15,11],"Olyimpque Lyon"),
    Midfielder("Arthur",8,[14,12,13,14,9],"Olyimpque Lyon"),
    Midfielder("Bosquets",5,[8,17,15,11,12],"Olyimpque Lyon"),
    Midfielder("Rackitic",4,[16,10,13,16,11],"Olyimpque Lyon"),
    Forward("Coutinho",14,[17,9,14,18,11],"Olyimpque Lyon"),
    Forward("Suarez",9,[19,9,15,17,17],"Olyimpque Lyon"),
    Forward("Messi",10,[20,6,14,20,11],"Olympique Lyon"),

    Goalie("Courtois",1,[17,17],"Real Madrid"),
    Defender("Marcelo",18,[14,12,17,15,15],"Real Madrid"),
    Defender("Varane",23,[7,16,14,14,14],"Real Madrid"),
    Defender("Ramos",3,[10,16,11,16,14],"Real Madrid"),
    Defender("Carvajal",20,[13,12,15,15,11],"Real Madrid"),
    Midfielder("Kroos",8,[14,12,13,14,9],"Real Madrid"),
    Midfielder("Casemerio",5,[8,17,15,11,12],"Real Madrid"),
    Midfielder("Modric",4,[16,10,13,16,11],"Real Madrid"),
    Forward("Isco Alcarcon",14,[17,9,14,18,11],"Real Madrid"),
    Forward("Benzema",9,[19,9,15,17,17],"Real Madrid"),
    Forward("Bale",10,[20,6,14,20,11],"Real Madrid"),

    Goalie("Ter Stegen",1,[17,17],"Pizen"),
    Defender("Alba",18,[14,12,17,15,15],"Pizen"),
    Defender("Umtiti",23,[7,16,14,14,14],"Pizen"),
    Defender("Pique",3,[10,16,11,16,14],"Pizen"),
    Defender("Roberto",20,[13,12,15,15,11],"Pizen"),
    Midfielder("Arthur",8,[14,12,13,14,9],"Pizen"),
    Midfielder("Bosquets",5,[8,17,15,11,12],"Pizen"),
    Midfielder("Rackitic",4,[16,10,13,16,11],"Pizen"),
    Forward("Coutinho",14,[17,9,14,18,11],"Pizen"),
    Forward("Suarez",9,[19,9,15,17,17],"Pizen"),
    Forward("Messi",10,[20,6,14,20,11],"Pizen"),

    Goalie("Ter Stegen",1,[17,17],"AS Roma"),
    Defender("Alba",18,[14,12,17,15,15],"AS Roma"),
    Defender("Umtiti",23,[7,16,14,14,14],"AS Roma"),
    Defender("Pique",3,[10,16,11,16,14],"AS Roma"),
    Defender("Roberto",20,[13,12,15,15,11],"AS Roma"),
    Midfielder("Arthur",8,[14,12,13,14,9],"AS Roma"),
    Midfielder("Bosquets",5,[8,17,15,11,12],"AS Roma"),
    Midfielder("Rackitic",4,[16,10,13,16,11],"AS Roma"),
    Forward("Coutinho",14,[17,9,14,18,11],"AS Roma"),
    Forward("Suarez",9,[19,9,15,17,17],"AS Roma"),
    Forward("Messi",10,[20,6,14,20,11],"AS Roma"),

    Goalie("Ter Stegen",1,[17,17],"Hoffenheim"),
    Defender("Alba",18,[14,12,17,15,15],"Hoffenheim"),
    Defender("Umtiti",23,[7,16,14,14,14],"Hoffenheim"),
    Defender("Pique",3,[10,16,11,16,14],"Hoffenheim"),
    Defender("Roberto",20,[13,12,15,15,11],"Hoffenheim"),
    Midfielder("Arthur",8,[14,12,13,14,9],"Hoffenheim"),
    Midfielder("Bosquets",5,[8,17,15,11,12],"Hoffenheim"),
    Midfielder("Rackitic",4,[16,10,13,16,11],"Hoffenheim"),
    Forward("Coutinho",14,[17,9,14,18,11],"Hoffenheim"),
    Forward("Suarez",9,[19,9,15,17,17],"Hoffenheim"),
    Forward("Messi",10,[20,6,14,20,11],"Hoffenheim"),

    Goalie("Ter Stegen",1,[17,17],"CSKA Moscow"),
    Defender("Alba",18,[14,12,17,15,15],"CSKA Moscow"),
    Defender("Umtiti",23,[7,16,14,14,14],"CSKA Moscow"),
    Defender("Pique",3,[10,16,11,16,14],"CSKA Moscow"),
    Defender("Roberto",20,[13,12,15,15,11],"CSKA Moscow"),
    Midfielder("Bosquets",5,[8,17,15,11,12],"CSKA Moscow"),
    Midfielder("Rackitic",4,[16,10,13,16,11],"CSKA Moscow"),
    Forward("Coutinho",14,[17,9,14,18,11],"CSKA Moscow"),
    Forward("Suarez",9,[19,9,15,17,17],"CSKA Moscow"),
    Forward("Messi",10,[20,6,14,20,11],"CSKA Moscow"),

    Goalie("Szczesny",1,[17,17],"Juventus"),
    Defender("Alex Sandro",18,[14,12,17,15,15],"Juventus"),
    Defender("Chellini",23,[7,16,14,14,14],"Juventus"),
    Defender("Bonnuci",3,[10,16,11,16,14],"Juventus"),
    Defender("De Sicligio",20,[13,12,15,15,11],"Juventus"),
    Midfielder("Matuidi",8,[14,12,13,14,9],"Juventus"),
    Midfielder("Pjanic",5,[8,17,15,11,12],"Juventus"),
    Midfielder("Khedira",4,[16,10,13,16,11],"Juventus"),
    Forward("Ronaldo",14,[17,9,14,18,11],"Juventus"),
    Forward("Mandzukic",9,[19,9,15,17,17],"Juventus"),
    Forward("Dybala",10,[20,6,14,20,11],"Juventus"),

    Goalie("De Gea",1,[17,17],"Manchester United"),
    Defender("Shaw",23,[14,12,17,15,15],"Manchester United"),
    Defender("Lindelof",2,[7,16,14,14,14],"Manchester United"),
    Defender("Smalling",12,[10,16,11,16,14],"Manchester United"),
    Defender("Young",18,[13,12,15,15,11],"Manchester United"),
    Midfielder("Pogba",6,[14,12,13,14,9],"Manchester United"),
    Midfielder("Matic",31,[8,17,15,11,12],"Manchester United"),
    Midfielder("Herrera",21,[16,10,13,16,11],"Manchester United"),
    Forward("Martial",11,[17,9,14,18,11],"Manchester United"),
    Forward("Lukaku",9,[19,9,15,17,17],"Manchester United"),
    Forward("Alexis",7,[20,6,14,20,11],"Manchester United"),

    Goalie("Ter Stegen",1,[17,17],"Valencia"),
    Defender("Alba",18,[14,12,17,15,15],"Valencia"),
    Defender("Umtiti",23,[7,16,14,14,14],"Valencia"),
    Defender("Pique",3,[10,16,11,16,14],"Valencia"),
    Defender("Roberto",20,[13,12,15,15,11],"Valencia"),
    Midfielder("Arthur",8,[14,12,13,14,9],"Valencia"),
    Midfielder("Bosquets",5,[8,17,15,11,12],"Valencia"),
    Midfielder("Rackitic",4,[16,10,13,16,11],"Valencia"),
    Forward("Coutinho",14,[17,9,14,18,11],"Valencia"),
    Forward("Suarez",9,[19,9,15,17,17],"Valencia"),
    Forward("Messi",10,[20,6,14,20,11],"Valencia"),

    Goalie("Ter Stegen",1,[17,17],"Young Boys"),
    Defender("Alba",18,[14,12,17,15,15],"Young Boys"),
    Defender("Umtiti",23,[7,16,14,14,14],"Young Boys"),
    Defender("Pique",3,[10,16,11,16,14],"Young Boys"),
    Defender("Roberto",20,[13,12,15,15,11],"Young Boys"),
    Midfielder("Arthur",8,[14,12,13,14,9],"Young Boys"),
    Midfielder("Bosquets",5,[8,17,15,11,12],"Young Boys"),
    Midfielder("Rackitic",4,[16,10,13,16,11],"Young Boys"),
    Forward("Coutinho",14,[17,9,14,18,11],"Young Boys"),
    Forward("Suarez",9,[19,9,15,17,17],"Young Boys"),
    Forward("Messi",10,[20,6,14,20,11],"Young Boys"),

    Goalie("Ter Stegen",1,[17,17],"Lokomotiv Moscow"),
    Defender("Alba",18,[14,12,17,15,15],"Lokomotiv Moscow"),
    Defender("Umtiti",23,[7,16,14,14,14],"Lokomotiv Moscow"),
    Defender("Pique",3,[10,16,11,16,14],"Lokomotiv Moscow"),
    Defender("Roberto",20,[13,12,15,15,11],"Lokomotiv Moscow"),
    Midfielder("Arthur",8,[14,12,13,14,9],"Lokomotiv Moscow"),
    Midfielder("Bosquets",5,[8,17,15,11,12],"Lokomotiv Moscow"),
    Midfielder("Rackitic",4,[16,10,13,16,11],"Lokomotiv Moscow"),
    Forward("Coutinho",14,[17,9,14,18,11],"Lokomotiv Moscow"),
    Forward("Suarez",9,[19,9,15,17,17],"Lokomotiv Moscow"),
    Forward("Messi",10,[20,6,14,20,11],"Lokomotiv Moscow")
    ]
    
    
    
def getPlayersofTeams(teams, players):
    for team in teams:
        team.players=[[],[],[],[]]
        for player in players:
            if player.team==team.name:
                if isinstance(player,Goalie):
                    team.players[0].append(player)
                elif isinstance(player,Defender):
                     team.players[1].append(player)
                elif isinstance(player,Midfielder):
                    team.players[2].append(player)
                else:
                    team.players[3].append(player)
    return teams
    
def generateGame():
    teams=getTeams()
    players=getPlayers()
    teams=getPlayersofTeams(teams,players)
    for team in teams:
        team.getTeamAvg()
    return teams

