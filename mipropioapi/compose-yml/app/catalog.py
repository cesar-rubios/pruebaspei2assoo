def get_products():
	fake_response = [{
		"title": "Vanilla icecream",
		"long_description": "helado claramente de vainilla",
		"price_euro": 1.5
	},{
		"title": "Cola icecream",
		"long_description": "helado claramente de cola",
		"price_euro": 1.5
	},{
		"title": "Chocolate icecream",
		"long_description": "helado claramente de chocolate",
		"price_euro": 2.5
	},{
		"title": "Lemon icecream",
		"long_description": "helado claramente de limón",
		"price_euro": 0.5
	}]
	return fake_response

def create_product(sku, title, long_description, price_euro):
	return "Hemos creado tu producto \n"