import pytest
from inventario import InventoryService, InsufficientStockException

def test_stock_negativo_lanza_excepcion():
    s = InventoryService({"P1": 5})
    with pytest.raises(InsufficientStockException):
        s.update_stock("P1", -10)

def test_retiro_valido_actualiza_stock():
    s = InventoryService({"P1": 5})
    s.update_stock("P1", -3)
    assert s.stock["P1"] == 2

def test_producto_inexistente_lanza_excepcion():
    s = InventoryService({"P1": 5})
    with pytest.raises(ValueError):
        s.update_stock("P99", 1)
        
