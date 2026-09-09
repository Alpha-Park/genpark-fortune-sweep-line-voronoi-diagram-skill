"""
Autonomous Agent Delaunay Triangulation & Voronoi Engine Skill
Pure Python Standard Library implementation.
"""
from typing import List, Tuple, Dict, Any

class DelaunayTriangulation2D:
    """
    Bowyer-Watson incremental Delaunay Triangulation in 2D.
    """
    @staticmethod
    def circumcircle_contains(tri: Tuple[Tuple[float, float], ...], point: Tuple[float, float]) -> bool:
        (x1, y1), (x2, y2), (x3, y3) = tri
        xp, yp = point
        d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        if abs(d) < 1e-9:
            return False
        ux = ((x1**2 + y1**2) * (y2 - y3) + (x2**2 + y2**2) * (y3 - y1) + (x3**2 + y3**2) * (y1 - y2)) / d
        uy = ((x1**2 + y1**2) * (x3 - x2) + (x2**2 + y2**2) * (x1 - x3) + (x3**2 + y3**2) * (x2 - x1)) / d
        r_sq = (x1 - ux)**2 + (y1 - uy)**2
        dist_sq = (xp - ux)**2 + (yp - uy)**2
        return dist_sq <= r_sq + 1e-9

    @staticmethod
    def triangulate(points: List[Tuple[float, float]]) -> List[Tuple[Tuple[float, float], ...]]:
        if len(points) < 3:
            return []
        min_x = min(p[0] for p in points) - 100
        max_x = max(p[0] for p in points) + 100
        min_y = min(p[1] for p in points) - 100
        max_y = max(p[1] for p in points) - 100

        st1 = (min_x, min_y)
        st2 = (max_x + (max_x - min_x), min_y)
        st3 = (min_x, max_y + 1000)
        super_tri = (st1, st2, st3)

        triangles = [super_tri]

        for p in points:
            bad_triangles = []
            for t in triangles:
                if DelaunayTriangulation2D.circumcircle_contains(t, p):
                    bad_triangles.append(t)

            edges = []
            for t in bad_triangles:
                for i in range(3):
                    edge = tuple(sorted((t[i], t[(i + 1) % 3])))
                    if edge in edges:
                        edges.remove(edge)
                    else:
                        edges.append(edge)

            for t in bad_triangles:
                triangles.remove(t)

            for e in edges:
                triangles.append((e[0], e[1], p))

        super_verts = {st1, st2, st3}
        return [t for t in triangles if not any(v in super_verts for v in t)]
