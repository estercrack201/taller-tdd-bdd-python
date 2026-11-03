# language: es
Característica: Registro de cotizaciones
  Como jefe de compras
  Quiero registrar cotizaciones de proveedores
  Para comparar ofertas sobre una solicitud activa

  Escenario: Registrar una cotización válida
    Dado un proveedor existente con NIT "900123456"
    Y una solicitud de cotización "SC-001" en estado "ABIERTA"
    Cuando el proveedor registra una cotización por 2500000
    Entonces la cotización queda en estado "RECIBIDA"
    Y el monto cotizado es 2500000
