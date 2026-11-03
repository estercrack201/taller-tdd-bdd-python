import pytest
from cotizacion_service import QuotationService, InvalidQuotationException


@pytest.fixture
def service():
    s = QuotationService()
    s.agregar_proveedor("900123456")
    s.agregar_solicitud("SC-001", "ABIERTA")
    s.agregar_solicitud("SC-002", "CERRADA")
    return s


def test_rechaza_proveedor_inexistente(service):
    with pytest.raises(InvalidQuotationException):
        service.registrar_cotizacion("999999999", "SC-001", 1000)


def test_rechaza_solicitud_cerrada(service):
    with pytest.raises(InvalidQuotationException):
        service.registrar_cotizacion("900123456", "SC-002", 1000)


@pytest.mark.parametrize("monto", [0, -1000])
def test_rechaza_monto_invalido(service, monto):
    with pytest.raises(InvalidQuotationException):
        service.registrar_cotizacion("900123456", "SC-001", monto)
