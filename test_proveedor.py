import unittest
from proveedor_service import SupplierService, InvalidSupplierException

class TestSupplierService(unittest.TestCase):

    def test_crea_proveedor_con_datos_validos(self):
        service = SupplierService()
        proveedor = service.create_supplier("900123456", "ACME S.A.S.", "contacto@acme.com")
        self.assertEqual(proveedor["nit"], "900123456")

    def test_rechaza_nit_invalido(self):
        service = SupplierService()
        with self.assertRaises(InvalidSupplierException):
            service.create_supplier("123", "ACME S.A.S.", "contacto@acme.com")

    def test_rechaza_correo_invalido(self):
        service = SupplierService()
        with self.assertRaises(InvalidSupplierException):
            service.create_supplier("900123456", "ACME S.A.S.", "sin-arroba.com")

    def test_rechaza_correos_mal_formados(self):
        service = SupplierService()
        for correo in ["usuario@", "@acme.com", "a@b"]:
            with self.subTest(correo=correo):
                with self.assertRaises(InvalidSupplierException):
                    service.create_supplier("900123456", "ACME S.A.S.", correo)
