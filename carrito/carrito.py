class Carro():
	def __init__(self,request):
		self.request = request
		self.session = self.request.session
		carrito = self.session.get('carro')

		if not carrito:
			self.carrito = self.session['carro']={}
		else:
			self.carrito = carrito
  
   
	def agregarProductos(self,producto):
		if (str(producto.id) not in self.carrito.keys()):
			self.carrito[producto.id]={
				'id':producto.id,
				'nombre':producto.nombre,
				'precio':str(producto.precio),
				'cantidad':1,
				'imagen':producto.imagen.url
			} 
		else:			
			self.carrito[str(producto.id)]['cantidad'] += 1

			self.carrito[str(producto.id)]['precio'] = float(self.carrito[str(producto.id)]['precio']) + producto.precio


		self.guardarProductos()	

	def guardarProductos(self):
		self.session['carro'] = self.carrito
		self.session.modified=True


	def eliminarProductos(self,producto):
		self.carrito.pop(str(producto.id))
		self.guardarProductos()	

	def restarUnidades(self,producto):
 
		if self.carrito[str(producto.id)]['cantidad']>0:
			self.carrito[str(producto.id)]['cantidad'] -= 1
			self.carrito[str(producto.id)]['precio'] = float(self.carrito[str(producto.id)]['precio']) - producto.precio

		
		if self.carrito[str(producto.id)]['cantidad']==0:
			self.eliminarProductos(producto)		

 
		self.guardarProductos()		

	def vaciarCarrito(self):
		
		self.carrito.clear()
		self.guardarProductos()	 