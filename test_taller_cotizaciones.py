import pytest
from unittest.mock import MagicMock
from cotizacion_service import QuotationService, InvalidQuotationException


@pytest.fixture
def repo():
    r = MagicMock()
    r.existe_cotizacion.return_value = False
    return r


@pytest.fixture
def service(repo):
    s = QuotationService(repo=repo)
    s.agregar_proveedor("900123456")
    s.agregar_solicitud("SC-001", "ABIERTA")
    return s


@pytest.mark.parametrize("monto", [0, -1000])
def test_monto_invalido_lanza_excepcion_y_no_guarda(service, repo, monto):
    with pytest.raises(InvalidQuotationException):
        service.registrar_cotizacion("900123456", "SC-001", monto)
    repo.save.assert_not_called()


def test_monto_valido_guarda_la_cotizacion(service, repo):
    cotizacion = service.registrar_cotizacion("900123456", "SC-001", 2500000)
    assert cotizacion["estado"] == "RECIBIDA"
    repo.save.assert_called_once()


def test_rechaza_cotizacion_duplicada(service, repo):
    repo.existe_cotizacion.return_value = True
    with pytest.raises(InvalidQuotationException):
        service.registrar_cotizacion("900123456", "SC-001", 2500000)
    repo.save.assert_not_called()
