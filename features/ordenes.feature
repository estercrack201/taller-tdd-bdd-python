# language: es
Característica: Aprobación de órdenes de compra
  Como jefe de compras
  Quiero aprobar órdenes de compra dentro del presupuesto del proveedor
  Para controlar el gasto

  Escenario: Aprobar orden dentro del presupuesto
    Dado el proveedor "ACME" con presupuesto disponible de 10000000
    Y una orden "OC-100" por 5000000 en estado "PENDIENTE"
    Cuando el jefe de compras aprueba la orden
    Entonces la orden cambia a "APROBADA"
    Y el presupuesto del proveedor se reduce a 5000000
