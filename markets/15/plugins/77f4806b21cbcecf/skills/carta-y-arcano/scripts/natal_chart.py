#!/usr/bin/env python3
"""Calculate natal tropical positions with Swiss Ephemeris (Moshier) and Placidus houses.
Dependencies: pyswisseph, timezonefinder; network for geocoding unless coords supplied.
Usage: python natal_chart.py --date 1985-07-02 --time 08:05 --city Porto --country Portugal
Optional: --lat 41.1579 --lon -8.6291 --timezone Europe/Lisbon (offline execution).
"""
import argparse, datetime as dt, json, math, urllib.parse, urllib.request
from zoneinfo import ZoneInfo
import swisseph as swe

SIGNS=['Aries','Tauro','Géminis','Cáncer','Leo','Virgo','Libra','Escorpio','Sagitario','Capricornio','Acuario','Piscis']
BODIES={'Sol':swe.SUN,'Luna':swe.MOON,'Mercurio':swe.MERCURY,'Venus':swe.VENUS,'Marte':swe.MARS,'Júpiter':swe.JUPITER,'Saturno':swe.SATURN,'Urano':swe.URANUS,'Neptuno':swe.NEPTUNE,'Plutón':swe.PLUTO,'Nodo norte verdadero':swe.TRUE_NODE}
ASPECTS={'conjunción':(0,8),'sextil':(60,4),'cuadratura':(90,6),'trígono':(120,6),'oposición':(180,8)}
def locate(city,country):
    query=urllib.parse.urlencode({'q':f'{city}, {country}','format':'jsonv2','limit':1})
    req=urllib.request.Request('https://nominatim.openstreetmap.org/search?'+query,headers={'User-Agent':'CartaYArcanoNatal/1.0 (contact: plugin developer)'})
    with urllib.request.urlopen(req,timeout=12) as response: data=json.load(response)
    if not data: raise ValueError('Localidad no encontrada; facilita coordenadas o revisa el nombre.')
    return float(data[0]['lat']),float(data[0]['lon']),data[0]['display_name']
def sign_degree(lon):
    lon=lon%360
    return {'signo':SIGNS[int(lon//30)],'grado_en_signo':round(lon%30,4),'longitud_ecliptica':round(lon,5)}
def house_index(lon,cusps):
    # Traversal across the ecliptic, handling wraparound at Aries.
    for i in range(12):
        a=cusps[i]%360;b=cusps[(i+1)%12]%360
        if (lon-a)%360 < (b-a)%360: return i+1
    return None

def calculate(args):
    latitude=args.lat;longitude=args.lon;place=args.city+', '+args.country
    if latitude is None or longitude is None:
        latitude,longitude,place=locate(args.city,args.country)
    timezone=args.timezone
    if not timezone:
        try: from timezonefinder import TimezoneFinder
        except ImportError as exc: raise RuntimeError('Instala timezonefinder para resolver automáticamente la zona horaria.') from exc
        timezone=TimezoneFinder().timezone_at(lat=latitude,lng=longitude)
    if not timezone: raise RuntimeError('No se pudo determinar automáticamente la zona horaria.')
    local=dt.datetime.fromisoformat(args.date+'T'+args.time).replace(tzinfo=ZoneInfo(timezone))
    utc=local.astimezone(dt.timezone.utc)
    hour=utc.hour+utc.minute/60+utc.second/3600+utc.microsecond/3.6e9
    jd=swe.julday(utc.year,utc.month,utc.day,hour,swe.GREG_CAL)
    values={}
    for name,body in BODIES.items():
        pos,flag=swe.calc_ut(jd,body,swe.FLG_MOSEPH|swe.FLG_SPEED)
        values[name]={'posicion':sign_degree(pos[0]),'retrogrado':pos[3]<0}
    north=values['Nodo norte verdadero']['posicion']['longitud_ecliptica']
    values['Nodo sur verdadero']={'posicion':sign_degree((north+180)%360),'retrogrado':values['Nodo norte verdadero']['retrogrado']}
    angles={};houses=[];house_note=None
    if not args.unknown_time:
        try:
            cusps,ascmc=swe.houses_ex(jd,latitude,longitude,b'P',swe.FLG_MOSEPH)
            houses=[{'casa':i+1,'posicion':sign_degree(c)} for i,c in enumerate(cusps)]
            angles={'Ascendente':{'posicion':sign_degree(ascmc[0])},'Medio Cielo':{'posicion':sign_degree(ascmc[1])}}
            for body in values.values(): body['casa']=house_index(body['posicion']['longitud_ecliptica'],cusps)
        except swe.Error:
            house_note='Casas Placidus no disponibles para estas coordenadas; posiciones planetarias calculadas sin casas.'
    selected=['Sol','Luna','Mercurio','Venus','Marte','Júpiter','Saturno','Urano','Neptuno','Plutón']
    aspects=[]
    for i,a in enumerate(selected):
        for b in selected[i+1:]:
            al=values[a]['posicion']['longitud_ecliptica'];bl=values[b]['posicion']['longitud_ecliptica']
            delta=abs((al-bl+180)%360-180)
            for name,(exact,orb) in ASPECTS.items():
                if abs(delta-exact)<=orb: aspects.append({'entre':[a,b],'aspecto':name,'orbe_grados':round(abs(delta-exact),3)})
    return {'localidad':place,'coordenadas':{'latitud':latitude,'longitud':longitude},'hora_local_aplicada':local.isoformat(),'utc_calculado':utc.isoformat(),'zona_iana_automatica':timezone,'zodiaco':'tropical','casas':'Placidus' if houses else None,'efemerides':'Swiss Ephemeris, algoritmo Moshier (pyswisseph)','posiciones':values,'angulos':angles,'cuspides':houses,'aspectos':sorted(aspects,key=lambda a:a['orbe_grados']),'aviso_casas':house_note}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--date',required=True,help='AAAA-MM-DD')
    p.add_argument('--time',required=True,help='HH:MM en hora local del lugar natal')
    p.add_argument('--city',required=True);p.add_argument('--country',required=True)
    p.add_argument('--lat',type=float);p.add_argument('--lon',type=float)
    p.add_argument('--timezone',help='IANA, solamente para uso interno o cuando ya se conoce')
    p.add_argument('--unknown-time',action='store_true')
    args=p.parse_args()
    if (args.lat is None)!=(args.lon is None): p.error('--lat y --lon deben facilitarse conjuntamente')
    try: print(json.dumps(calculate(args),ensure_ascii=False,indent=2))
    except Exception as ex: p.exit(2,'Error de cálculo natal: '+str(ex)+'\n')
if __name__=='__main__':main()
