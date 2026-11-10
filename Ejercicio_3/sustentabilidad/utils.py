def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    """
    Calcula las emisiones de carbono industriales.
    Eleva ValueError si el consumo es negativo.
    """
    if consumo_kwh < 0:
        raise ValueError("El consumo en kWh no puede ser negativo.")
    return consumo_kwh * factor_emision


def obtener_metricas_consumo(registros):
    """
    Procesa un historial de consumos por planta industrial para determinar 
    el total global de emisiones y la planta de mayor consumo.
    """
    if not registros:
        return {"total_emisiones": 0.0, "planta_mayor_consumo": None}
        
    total_emisiones = 0.0
    max_consumo = -1
    planta_mayor = None
    
    for reg in registros:
        planta = reg.get("planta")
        consumo = reg.get("consumo", 0)
        
        emisiones = calcular_emisiones_carbono(consumo)
        total_emisiones += emisiones
        
        if consumo > max_consumo:
            max_consumo = consumo
            planta_mayor = planta
            
    return {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor
    }