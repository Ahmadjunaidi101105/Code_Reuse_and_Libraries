class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "CIRCLE":
            return "Ini adalah lingkaran"
        elif shape_type == " SQUARE":
            return "Ini adalah persegi"
        elif shape_type == "RECTANGLE":
            return "Ini adalah persegi panjang"
        else:
            raise ValueError("Unknown shape type")
        
print(ShapeFactory.get_shape("CIRCLE"))
print(ShapeFactory.get_shape("SQUARE"))
print(ShapeFactory.get_shape("RECTANGLE"))