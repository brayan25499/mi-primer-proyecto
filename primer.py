# tareas.py · Seguimiento del proyecto LevelUPGym

pendientes = [
    "Implementar recuperación de contraseña",
    "Crear panel administrativo",
    "Desplegar la aplicación en un servidor",
]

completadas = [
    "Configuración del repositorio con Git y GitHub",
    "Diseño inicial de la base de datos",
    "Estructura básica del frontend",
]

en_progreso = [
    "Implementación del login y registro de usuarios",
    "Conexión entre frontend y backend",
    "Gestión de membresías del gimnasio",
]

print("=" * 40)
print("SEGUIMIENTO DEL PROYECTO LEVELUPGYM")
print("=" * 40)

print("\n✅ COMPLETADAS:")
for t in completadas:
    print(f"   ✅ {t}")

print("\n🔧 EN PROGRESO:")
for t in en_progreso:
    print(f"   🔧 {t}")

print("\n⬜ PENDIENTES:")
for t in pendientes:
    print(f"   ⬜ {t}")

print("\n" + "=" * 40)
print(f"Total tareas: {len(completadas) + len(en_progreso) + len(pendientes)}")
print(f"Completadas:  {len(completadas)}")
print(f"Pendientes:   {len(pendientes)}")