import re

class InvalidSupplierException(Exception):
    pass

class SupplierHasActiveOrdersException(Exception):
    pass

class SupplierService:
    PATRON_CORREO = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    def __init__(self, repo_ordenes=None):
        self.repo_ordenes = repo_ordenes
        self.proveedores = {}

    def _validar_nit(self, nit):
        if nit is None or len(nit) < 9:
            raise InvalidSupplierException("NIT inválido")

    def _validar_correo(self, correo):
        if not correo or not self.PATRON_CORREO.match(correo):
            raise InvalidSupplierException("Correo inválido")

    def create_supplier(self, nit, nombre, correo):
        self._validar_nit(nit)
        self._validar_correo(correo)
        proveedor = {"nit": nit, "nombre": nombre, "correo": correo, "estado": "ACTIVO"}
        self.proveedores[nit] = proveedor
        return proveedor

    def delete_supplier(self, nit):
        if self.repo_ordenes.has_active_orders(nit):
            raise SupplierHasActiveOrdersException(
                "No se puede eliminar un proveedor con órdenes activas"
            )
        proveedor = self.proveedores[nit]
        proveedor["estado"] = "INACTIVO"
        return proveedor
