class InsufficientStockException(Exception):
    pass

class InventoryService:
    def __init__(self, stock):
        self.stock = stock

    def _obtener_stock(self, product_id):
        if product_id not in self.stock:
            raise ValueError(f"Producto {product_id} no existe")
        return self.stock[product_id]

    def update_stock(self, product_id, quantity):
        actual = self._obtener_stock(product_id)
        nuevo = actual + quantity
        if nuevo < 0:
            raise InsufficientStockException(
                f"Stock insuficiente para {product_id}: hay {actual}, se pidió {-quantity}"
            )
        self.stock[product_id] = nuevo

    def retirar(self, product_id, cantidad):
        self.update_stock(product_id, -cantidad)
        return "Retiro exitoso"
