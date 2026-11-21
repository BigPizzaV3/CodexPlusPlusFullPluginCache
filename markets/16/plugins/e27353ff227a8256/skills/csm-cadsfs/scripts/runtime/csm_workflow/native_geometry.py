"""Geometría de comprobación e integración. No cambia el Python del autor.

Triangulación propia por recorte de orejas para polígonos simples sin huecos.
Mantiene el orden de aristas y los grupos Wall 1..N del generador recibido.
No certifica acústica ni ejecuta el lector de CADSFS.
"""
from __future__ import annotations
from collections import Counter
import math
import numpy as np


class GeometryError(ValueError):
    pass


def number(value: object, *, positive: bool = False) -> float:
    if type(value) not in (int, float) or not math.isfinite(value):
        raise GeometryError('Se requiere un número finito.')
    value = float(value)
    if abs(value) > 1e6 or (positive and value <= 0):
        raise GeometryError('Magnitud no admitida.')
    return value


def cross(a, b, c) -> float:
    return float((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))


def area_signed(poly) -> float:
    return sum(poly[i][0]*poly[(i+1)%len(poly)][1] -
               poly[(i+1)%len(poly)][0]*poly[i][1] for i in range(len(poly))) / 2


def point_inside(p, poly, *, boundary: bool = True) -> bool:
    x, y = p
    inside = False
    eps = 1e-9 * max(1., max(abs(t) for q in poly for t in q))
    for a, b in zip(poly, poly[1:]+poly[:1]):
        if abs(cross(a,b,p)) <= eps and (min(a[0],b[0])-eps <= x <= max(a[0],b[0])+eps and
                                         min(a[1],b[1])-eps <= y <= max(a[1],b[1])+eps):
            return boundary
        if (a[1] > y) != (b[1] > y):
            if x < (b[0]-a[0])*(y-a[1])/(b[1]-a[1])+a[0]:
                inside = not inside
    return inside


def prepare_polygon(raw) -> list[list[float]]:
    if not isinstance(raw, (list, tuple)) or not 3 <= len(raw) <= 512:
        raise GeometryError('Se requieren 3 a 512 vértices de un polígono simple.')
    if any(not isinstance(p, (list, tuple)) or len(p) != 2 for p in raw):
        raise GeometryError('Cada vértice necesita dos coordenadas.')
    poly = [[number(x), number(y)] for x,y in raw]
    scale = max(1., max(abs(t) for p in poly for t in p))
    eps = 1e-11 * scale * scale
    if len({tuple(p) for p in poly}) != len(poly):
        raise GeometryError('No repetir vértices, tampoco el primero al cerrar.')
    if abs(area_signed(poly)) <= eps:
        raise GeometryError('Polígono de área nula.')
    n = len(poly)
    for i in range(n):
        if abs(cross(poly[i-1],poly[i],poly[(i+1)%n])) <= eps:
            raise GeometryError('Simplificar vértices consecutivos colineales.')
    def intersect(a,b,c,d):
        c1,c2,c3,c4 = cross(a,b,c),cross(a,b,d),cross(c,d,a),cross(c,d,b)
        if ((c1>eps and c2<-eps) or (c1<-eps and c2>eps)) and ((c3>eps and c4<-eps) or (c3<-eps and c4>eps)):
            return True
        for v,u,w,t in ((c,a,b,c1),(d,a,b,c2),(a,c,d,c3),(b,c,d,c4)):
            if abs(t)<=eps and min(u[0],w[0])-eps<=v[0]<=max(u[0],w[0])+eps and min(u[1],w[1])-eps<=v[1]<=max(u[1],w[1])+eps:
                return True
        return False
    for i in range(n):
        for j in range(i+1,n):
            if j == i+1 or (i==0 and j==n-1):
                continue
            if intersect(poly[i],poly[(i+1)%n],poly[j],poly[(j+1)%n]):
                raise GeometryError('El perímetro se cruza o toca a sí mismo.')
    return poly


def triangulate(poly) -> np.ndarray:
    """Triángulos CCW; los índices siempre refieren al perímetro original."""
    poly = prepare_polygon(poly)
    ids = list(range(len(poly)))
    if area_signed(poly)<0:
        ids.reverse()
    eps=1e-11*max(1.,max(abs(t) for p in poly for t in p))**2
    triangles=[]
    while len(ids)>3:
        ear=False
        for k,b in enumerate(ids):
            a,c=ids[k-1],ids[(k+1)%len(ids)]
            if cross(poly[a],poly[b],poly[c])<=eps:
                continue
            if any(min(cross(poly[a],poly[b],poly[j]),cross(poly[b],poly[c],poly[j]),cross(poly[c],poly[a],poly[j]))>=-eps
                   for j in ids if j not in (a,b,c)):
                continue
            triangles.append([a,b,c]); del ids[k]; ear=True; break
        if not ear:
            raise GeometryError('No se pudo triangular sin alterar el perímetro.')
    triangles.append(ids)
    return np.asarray(triangles,dtype=np.int32)


def extrusion(poly, height):
    poly=prepare_polygon(poly); height=number(height,positive=True)
    cap=triangulate(poly); n=len(poly)
    v=np.asarray([[x,y,z] for z in (0.,height) for x,y in poly],dtype=np.float64)
    faces=[list(t[::-1]) for t in cap]+[list(t+n) for t in cap]
    groups=[0]*len(cap)+[1]*len(cap)
    ccw=area_signed(poly)>0
    for i in range(n):
        j=(i+1)%n
        side=[[i,j,j+n],[i,j+n,i+n]]
        if not ccw:
            side=[t[::-1] for t in side]
        faces.extend(side); groups.extend([2+i,2+i])
    return v,np.asarray(faces,dtype=np.int32),np.asarray(groups,dtype=np.int32)


def check_extrusion(v, f, ftg, poly, height) -> dict:
    """Controles independientes de área, cierre orientado, volumen y perímetro."""
    v=np.asarray(v,dtype=float); f=np.asarray(f,dtype=int); ftg=np.asarray(ftg,dtype=int)
    expected_area=abs(area_signed(poly)); expected_volume=expected_area*height
    if v.ndim!=2 or v.shape[1]!=3 or not np.isfinite(v).all() or f.ndim!=2 or f.shape[1]!=3 or len(ftg)!=len(f):
        raise GeometryError('Malla mal formada.')
    if len(f)==0 or f.min()<0 or f.max()>=len(v):
        raise GeometryError('Índices de malla fuera de rango.')
    t=v[f]; normals=np.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]); areas=np.linalg.norm(normals,axis=1)/2
    edges=Counter((int(a),int(b)) for face in f for a,b in zip(face,np.roll(face,-1)))
    closed=all(count==1 and edges[(b,a)]==1 for (a,b),count in edges.items())
    floor_area=float(areas[ftg==0].sum()); ceiling_area=float(areas[ftg==1].sum())
    volume=float(np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2])).sum()/6)
    n=len(poly)
    expected_v=np.asarray([[x,y,z] for z in (0.,height) for x,y in poly])
    geometry_matches=(v.shape==expected_v.shape and np.allclose(v,expected_v,rtol=1e-7,atol=1e-6))
    cap_inside=all(point_inside(list(c[:2]),poly) for c in t[(ftg==0)|(ftg==1)].mean(axis=1))
    groups_match=all(np.allclose(v[np.unique(f[ftg==i+2])],expected_v[sorted({i,(i+1)%n,i+n,(i+1)%n+n})],atol=1e-6)
                     if len(np.unique(f[ftg==i+2]))==4 else False for i in range(n))
    ok=(geometry_matches and groups_match and cap_inside and closed and bool((areas>1e-10).all()) and
        math.isclose(floor_area,expected_area,rel_tol=1e-6,abs_tol=1e-6) and
        math.isclose(ceiling_area,expected_area,rel_tol=1e-6,abs_tol=1e-6) and
        math.isclose(volume,expected_volume,rel_tol=1e-6,abs_tol=1e-6) and
        bool((normals[ftg==0,2]<0).all()) and bool((normals[ftg==1,2]>0).all()))
    return {'ok':bool(ok),'floor_area_m2':floor_area,'ceiling_area_m2':ceiling_area,
            'expected_floor_area_m2':expected_area,'volume_m3':volume,'expected_volume_m3':expected_volume,
            'closed_oriented_edges':closed,'wall_groups_match_edges':bool(groups_match),'cap_centroids_inside':cap_inside}
