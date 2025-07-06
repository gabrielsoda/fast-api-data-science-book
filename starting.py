import sys
import pkg_resources

# Imprimir versión de Python
print(f"Python version: {sys.version}")

# Imprimir todas las dependencias instaladas
print("\nInstalled packages:")
for dist in pkg_resources.working_set:
    print(f"{dist.project_name}=={dist.version}")
