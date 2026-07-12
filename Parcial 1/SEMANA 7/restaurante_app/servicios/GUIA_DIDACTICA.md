# Guía didáctica - Restaurante App (Semana 7)

Este documento explica los conceptos aplicados en la capa de servicios:

## Clase Restaurante

- Administra listas de productos y clientes.
- Proporciona métodos para:
  - **Productos**: registrar_producto(), listar_productos(), buscar_producto()
  - **Clientes**: registrar_cliente(), listar_clientes(), buscar_cliente()
- Valida registros duplicados por nombre (productos) o ID (clientes).
- Método precargar_ejemplos() carga datos iniciales para demostración.

## Flujo esperado

input() usuario
  ↓
constructor del modelo
  ↓
creación del objeto
  ↓
registro en Restaurante
  ↓
listado o búsqueda

Lea el código en restaurante.py y comprenda cómo los modelos (Producto y Cliente)
se integran con el servicio principal.

