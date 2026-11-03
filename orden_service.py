class OrdenInvalidaException(Exception):
    pass


class OrdenService:
    def __init__(self):
        self.presupuestos = {}   # proveedor -> presupuesto disponible
        self.ordenes = {}        # codigo -> orden

    def agregar_proveedor(self, nombre, presupuesto):
        self.presupuestos[nombre] = presupuesto

    def agregar_orden(self, codigo, proveedor, monto, estado):
        self.ordenes[codigo] = {
            "codigo": codigo,
            "proveedor": proveedor,
            "monto": monto,
            "estado": estado,
        }

    def aprobar_orden(self, codigo):
        orden = self.ordenes[codigo]
        if orden["estado"] == "APROBADA":
            raise OrdenInvalidaException("La orden ya está aprobada")
        proveedor = orden["proveedor"]
        if orden["monto"] > self.presupuestos[proveedor]:
            raise OrdenInvalidaException("Excede el presupuesto del proveedor")
        self.presupuestos[proveedor] -= orden["monto"]
        orden["estado"] = "APROBADA"
        return orden

    def presupuesto_de(self, proveedor):
        return self.presupuestos[proveedor]
