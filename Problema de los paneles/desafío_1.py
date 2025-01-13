

def n_paneles_triangulo(base, altura, x_panel, y_panel):
    """
    Función que calcula el número de rectángulos que caben en un triángulo.
    :param base: int. Base del triángulo.
    :param altura: int. Altura del triángulo.
    :param x_panel: int. Longitud del panel en dirección x.
    :param y_panel: int. Longitud del panel en dirección y.
    :return: int. Número de paneles que caben dentro del triángulo.
    """
    # en primer lugar, hay que verificar si el triángulo es más alto que ancho
    if base < altura:
        mas_ancho = False
    else:
        mas_ancho = True
    
    # luego, si es más ancho que alto, tenemos que asegurarnos de que el panel esté orientado de manera horizontal
    if mas_ancho:
        if x_panel < y_panel:
            x_panel, y_panel = y_panel, x_panel
    # en caso contrario, habrá que asegurarse de que el panel esté orientado de manera vertical
    else:
        if x_panel > y_panel:
            x_panel, y_panel = y_panel, x_panel      

    total_rectangulos = 0
    altura_actual = 0

    # se itera mientras haya espacio vertical para al menos un rectángulo
    while altura_actual + y_panel <= altura:
        altura_actual += y_panel
        longitud_disponible = base * (1 - altura_actual / altura) # esta longitud se obtiene a partir de la semejanza entre ambos triángulos
        rectangulos_en_fila = int(longitud_disponible // x_panel)
        total_rectangulos += rectangulos_en_fila

    return total_rectangulos

if __name__ == '__main__':
    while True:
        try:
            base, altura, x_panel, y_panel = input("Ingresar las dimensiones del triángulo y del panel en formato base,altura,x_panel,y_panel: ").split(",")
            base = float(base)
            altura = float(altura)
            x_panel = float(x_panel)
            y_panel = float(y_panel)
            total = n_paneles_triangulo(base, altura, x_panel, y_panel)
            print(f"El número de paneles que caben en el triángulo es: {total}")
            break
        except Exception as e:
            hola = input(f"{e}")
            print("Por favor, ingresar valores enteros positivos en el formato pedido.\n")
