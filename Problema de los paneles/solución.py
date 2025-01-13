

def n_paneles(x_techo, y_techo, x_panel, y_panel):
    """
    Función que calcula el número de paneles sin rotar que caben en un rectángulo techo.
    :param x_techo: int. Longitud del techo en dirección x.
    :param y_techo: int. Longitud del techo en dirección y.
    :param x_panel: int. Longitud del panel en dirección x.
    :param y_panel: int. Longitud del panel en dirección y.
    :return: int. Número de paneles que caben dentro del rectángulo techo.
    """
    # primero se calcula el número de paneles que caben sin rotar el panel, formando un rectángulo de paneles
    n_x = x_techo // x_panel
    n_y = y_techo // y_panel
    total_inicial = n_x * n_y

    if x_techo % x_panel == 0 and y_techo % y_panel == 0:
        return int(total_inicial)

    # luego, dependiendo de las dimensiones del problema tenemos 3 casos:
    if x_panel < y_panel: # si el panel es más alto que ancho, la franja sobrante es horizontal
        x_franja = x_techo
        y_franja = y_techo % y_panel if y_techo % y_panel != 0 else 0
    elif x_panel > y_panel: # si es al revés, la franja es vertical
        x_franja = x_techo % x_panel if x_techo % x_panel != 0 else 0
        y_franja = y_techo
    else: # si el panel es cuadrado, no cabrán más paneles y retornamos el total inicial
        return int(total_inicial)

    # por último se calcula el número de paneles que caben en la franja sobrante rotando el panel y lo sumamos al total inicial
    n_x_franja = x_franja // y_panel
    n_y_franja = y_franja // x_panel
    total_franja = n_x_franja * n_y_franja

    total = total_inicial + total_franja

    return int(total)

def probar_rotacion(x_techo, y_techo, x_panel, y_panel):
    """
    Función que prueba si rotar el panel mejora la cantidad de paneles que caben en el techo.
    :param x_techo: int. Longitud del techo en dirección x.
    :param y_techo: int. Longitud del techo en dirección y.
    :param x_panel: int. Longitud del panel en dirección x.
    :param y_panel: int. Longitud del panel en dirección y.
    :return: int. Número de paneles que caben en el techo.
    """
    return max(n_paneles(x_techo, y_techo, x_panel, y_panel), n_paneles(x_techo, y_techo, y_panel, x_panel))

if __name__ == '__main__':
    while True:
        try:
            # x_techo, y_techo, x_panel, y_panel = input("Ingresar las dimensiones del techo y del panel en formato x_techo,y_techo,x_panel,y_panel: ").split(",")
            x_techo, y_techo, x_panel, y_panel = 5,4,2,3
            x_techo = float(x_techo)
            y_techo = float(y_techo)
            x_panel = float(x_panel)
            y_panel = float(y_panel)
            total = probar_rotacion(x_techo, y_techo, x_panel, y_panel)
            print(f"El número de paneles que caben en el techo es: {total}")
            break
        except:
            print("Por favor, ingresar valores enteros positivos en el formato pedido.\n")
            
