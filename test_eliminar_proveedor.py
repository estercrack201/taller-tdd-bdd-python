import unittest
from unittest.mock import MagicMock
from proveedor_service import SupplierService, SupplierHasActiveOrdersException


class TestEliminarProveedor(unittest.TestCase):

    def test_no_deberia_eliminar_con_ordenes_activas(self):
        repo_ordenes = MagicMock()
        repo_ordenes.has_active_orders.return_value = True
        service = SupplierService(repo_ordenes=repo_ordenes)
        with self.assertRaises(SupplierHasActiveOrdersException):
            service.delete_supplier("900123456")

    def test_deberia_desactivar_si_no_tiene_ordenes_activas(self):
        repo_ordenes = MagicMock()
        repo_ordenes.has_active_orders.return_value = False
        service = SupplierService(repo_ordenes=repo_ordenes)
        service.create_supplier("900123456", "ACME S.A.S.", "contacto@acme.com")
        proveedor = service.delete_supplier("900123456")
        self.assertEqual(proveedor["estado"], "INACTIVO")
