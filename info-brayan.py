
# info-proyecto.py
# Completa este archivo con los datos reales de tu proyecto
# Ejecutalo con: python info-proyecto.py

# ── DATOS DEL PROYECTO ──────────────────────────────────────
nombre_proyecto = "LevelUpGym"
descripcion = "Sistema web para administrar un gimnasio y sus usuarios"
tecnologias = ["HTML", "CSS", "Python", "Git", "GitHub"]
integrantes = ["Brayan Valencia"]

funcionalidades = [
    "Login de usuarios",
    "Registro de clientes",
    "Gestion de planes",
    "Dashboard administrativo",
]

estado = "En construccion"

# ── TAREAS DEL EQUIPO ────────────────────────────────────────
tareas_completadas = [
    "Diseno de base de datos",
    "Prototipo de interfaz",
    "Creacion del repositorio",
]

tareas_pendientes = [
    "Conectar frontend con backend",
    "Implementar autenticacion",
]

tareas_en_progreso = [
    "Diseno de pantallas principales",
]

# ── FUNCIONES ────────────────────────────────────────────────
def mostrar_info():
    print("=" * 45)
    print(f"  PROYECTO: {nombre_proyecto}")
    print("=" * 45)
    print(f"  Descripcion : {descripcion}")
    print(f"  Estado      : {estado}")
    print(f"  Tecnologias : {', '.join(tecnologias)}")
    print(f"  Integrantes : {', '.join(integrantes)}")

def mostrar_funcionalidades():
    print("\n  FUNCIONALIDADES:")
    for i, f in enumerate(funcionalidades, 1):
        print(f"    {i}. {f}")

def mostrar_tareas():
    print("\n  TAREAS COMPLETADAS:")
    for t in tareas_completadas:
        print(f"    [x] {t}")

    print("\n  EN PROGRESO:")
    for t in tareas_en_progreso:
        print(f"    [~] {t}")

    print("\n  PENDIENTES:")
    for t in tareas_pendientes:
        print(f"    [ ] {t}")

    total = len(tareas_completadas) + len(tareas_pendientes) + len(tareas_en_progreso)

    print(f"\n  Total tareas: {total} | Completadas: {len(tareas_completadas)}")

# ── EJECUTAR ─────────────────────────────────────────────────
mostrar_info()
mostrar_funcionalidades()
mostrar_tareas()

print("\n" + "=" * 45)
