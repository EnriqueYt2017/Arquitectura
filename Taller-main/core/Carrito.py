class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto):
        print(producto.image.url)
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "acumulado": producto.precio,
                "image": producto.image.url,
                "cantidad": 1,
            }
        else:
            if self.carrito[id]["cantidad"] >= 100:
                self.carrito[id]["cantidad"] = 100
                self.carrito[id]["acumulado"] = producto.precio * 100
            else:
                self.carrito[id]["cantidad"] += 1
                self.carrito[id]["acumulado"] += producto.precio
        self.guardar_carrito()

    def establecer(self, producto, cantidad):
        id = str(producto.id)
        if int(cantidad) > 100:
            cantidad = 100
        self.carrito[id]={
            "producto_id": producto.id,
            "nombre": producto.nombre,
            "acumulado": producto.precio * int(cantidad),
            "image": producto.image.url,
            "cantidad": int(cantidad),
        }
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
