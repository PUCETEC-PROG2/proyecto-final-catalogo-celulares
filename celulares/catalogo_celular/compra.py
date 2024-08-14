class Carrito:
    def __init__(self, request) -> None:
        self.request = request
        self.session = request.session
        compra = self.session.get("compra")
        if not compra:
            self.session["compra"] = {}
            self.compra = self.session["compra"]
        else:
            self.compra = compra

    def guardar_compra(self):
        self.session["compra"] = self.compra
        self.session.modified = True

    def agregar(self, producto):
        id = str(producto.id)
        price = float(producto.precio)
        if id not in self.compra.keys():
            self.compra[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre_producto,
                "precio": price,
                "cantidad": 1,
            }
        else:
            self.compra[id]["cantidad"] += 1
            self.compra[id]["acumulado"] = self.compra[id].get("acumulado", 0) + price

        self.guardar_compra()

    def eliminar_compra(self, producto):
        id = str(producto.id)
        if id in self.compra:
            del self.compra[id]
            self.guardar_compra()

    def restar (self, producto):
        id = str(producto.id)
        if id in self.compra.keys():
            self.compra[id]["cantidad"] -= 1
            self.compra[id]["acumulado"] -= producto.precio
            if self.compra[id]["cantidad"] <= 0:
                self.eliminar_compra(producto)
            self.guardar_compra()

    def limpiar(self):
        self.session["compra"] = {}
        self.session.modified = True