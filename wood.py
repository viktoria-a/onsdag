#coding: utf-8
#wood_price= 900
#wood_count= 2
#wood_vat= 1.25

#book_price= 100
#book_count=1
#book_vat=1.06

#print wood_price * wood_count * wood_vat + book_price * book_count * book_vat

#wood_companies_phone_number = ["070444388282", "0877839382", "0847390484"]
#print wood_companies_phone_number[2]

#wood_companies_by_name= { "Norrlands skog": "070444388282", 
#"Svea skog": "0877839382",
#u"Göta skog": "0847390484" }
#print wood_companies_by_name[u"Göta skog"]

#wood= {"price": 900, "count": 2, "vat": 1.25}
#book= {"price": 100, "count": 1, "vat": 1.06}
#print wood ["price"] * wood ["vat"] + book ["price"] * book ["vat"] 

#class Product(object): 
#	price=0
#	count=0
#	vat=0
#	def price_with_vat(self):
#		return self.price * self.count * self.vat

#wood=Product()
#wood.price=900
#wood.count=1
#wood.vat=1.25

#book=Product()
#book.price=100
#book.count=1
#book.vat=1.06

#print wood.price_with_vat() 	


class Product (object):
	def __init__ (self,price,count,vat):
		self.price=price
		self.count=count
		self.vat=vat

	def price_with_vat(self):
		total = self.price * self.count * self.vat
		if self.price >500:
			return 0.9 * total 
		else: return total
	def price_without_vat(self):
		return self.price
	def count_and_vat(self):
		return self.price + self.count


wood=Product (price=900, count=1, vat=1.25)
book=Product (price=100, count=10, vat=1.06)
bulldozer=Product (price=13000, count=1, vat=1.25)

#print wood.price_with_vat() + book.price_without_vat()
#print book.count_and_vat()

varor = [Product(price=100, count=1, vat=1.25), 
Product(price=100, count=10, vat=1.06), Product(price=13000, count=1, vat=1.25)]
total_price= varor [0].price_with_vat() + varor [1].price_with_vat() + varor [2].price_with_vat()

print total_price

varor = [Product(price=900, count=1, vat=1.25), 
Product(price=100, count=10, vat=1.06), Product(price=13000, count=1, vat=1.25)]
total_price= 0 
for product in varor:
	total_price +=product.price_with_vat()

print total_price



 
	
