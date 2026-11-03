import unittest
from inventario import InventoryService, InsufficientStockException


class TestRetiroInventario(unittest.TestCase):

    def test_retiro_de_inventario(self):
        casos = [
            # codigo, stock, retiro, final, mensaje
            ("PROD-001", 10, 3, 7, "Retiro exitoso"),
            ("PROD-002", 5, 5, 0, "Retiro exitoso"),
            ("PROD-003", 2, 5, 2, "Stock insuficiente"),
        ]
        for codigo, stock, retiro, final, mensaje in casos:
            with self.subTest(codigo=codigo):
                service = InventoryService({codigo: stock})
                try:
                    resultado = service.retirar(codigo, retiro)
                except InsufficientStockException as e:
                    resultado = "Stock insuficiente"
                self.assertEqual(resultado, mensaje)
                self.assertEqual(service.stock[codigo], final)
