import sympy as sp

# Define symbols
u, v = sp.symbols('u v', real=True)
denom = u**2 + v**2 + 4

# Parametrization X(u, v)
X = sp.Matrix([
    (4*u) / denom,
    (4*v) / denom,
    (2*(u**2 + v**2)) / denom
])

# Compute partials
Xu = X.diff(u)
Xv = X.diff(v)

# Compute cross product and norm
cross_prod = Xu.cross(Xv)
magnitude = sp.simplify(cross_prod.norm())

# Compute FFF coefficients
E = sp.simplify(Xu.dot(Xu))
F = sp.simplify(Xu.dot(Xv))
G = sp.simplify(Xv.dot(Xv))

print(f"Cross Product Magnitude: {magnitude}")
print(f"E: {E}")
print(f"F: {F}")
print(f"G: {G}")