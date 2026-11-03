class InvalidQuotationException(Exception):
    pass

class QuotationService:
    def __init__(self, repo=None):
        self.repo = repo
        self.proveedores = set()
        self.solicitudes = {}   # codigo -> estado
        self.cotizaciones = []

    def agregar_proveedor(self, nit):
        self.proveedores.add(nit)

    def agregar_solicitud(self, codigo, estado):
        self.solicitudes[codigo] = estado

    def registrar_cotizacion(self, nit, codigo_solicitud, monto):
        if nit not in self.proveedores:
            raise InvalidQuotationException("Proveedor no existe")
        if self.solicitudes.get(codigo_solicitud) != "ABIERTA":
            raise InvalidQuotationException("La solicitud no está abierta")
        if monto <= 0:
            raise InvalidQuotationException("Monto inválido")
        if self.repo and self.repo.existe_cotizacion(nit, codigo_solicitud):
            raise InvalidQuotationException("Cotización duplicada")
        cotizacion = {
            "nit": nit,
            "solicitud": codigo_solicitud,
            "monto": monto,
            "estado": "RECIBIDA",
        }
        self.cotizaciones.append(cotizacion)
        if self.repo:
            self.repo.save(cotizacion)
        return cotizacion
