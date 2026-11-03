# Taller TDD, BDD y Calidad Ágil con Python

Universidad de Cundinamarca · Sede Chía · Ingeniería de Sistemas y Computación

**Grupo:** T2

**Integrantes:**
- Bairon Steve Ferro Morales
- David Santiago Mendez Carrillo
- Erick Javier Sierra Martinez
- Esteban Alonso Umaña Velásquez

## Descripción
Incremento de software para la gestión de proveedores, cotizaciones,
órdenes de compra e inventario, desarrollado con TDD (unittest y pytest)
y BDD (Behave).

## Módulos
- `proveedor_service.py`: crear y desactivar proveedores
- `cotizacion_service.py`: registro de cotizaciones
- `orden_service.py`: aprobación de órdenes de compra
- `inventario.py`: control de stock

## Pruebas
- `test_*.py`: pruebas unitarias
- `features/`: escenarios BDD en Gherkin con sus step definitions

## Cómo ejecutar
    pip install pytest behave coverage
    pytest
    python -m unittest discover -p "test_*.py"
    behave

## Cobertura
`cotizacion_service.py` pasó de 86% a 100% al combinar Behave y pytest.
