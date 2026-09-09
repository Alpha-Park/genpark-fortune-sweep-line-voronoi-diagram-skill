"""Example usage for Delaunay Triangulation & Voronoi Skill."""
from client import DelaunayTriangulation2D

def main():
    print("Executing Delaunay Triangulation...")
    d_pts = [(0.0, 0.0), (2.0, 0.0), (1.0, 2.0), (1.0, 0.8)]
    tris = DelaunayTriangulation2D.triangulate(d_pts)
    print(f"Generated {len(tris)} Delaunay Triangles:")
    for t in tris:
        print(" ", t)
    assert len(tris) >= 1, "Expected at least 1 triangle"
    print("Delaunay Triangulation verified successfully!")

if __name__ == "__main__":
    main()
