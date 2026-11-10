# ejercicio_1/sensores.py

def limpiar_registro_sensor(registro_raw):
    """
    Procesa un diccionario con datos crudos de un sensor, normalizando
    el identificador, la temperatura (como float limpio) y la ubicación.
    """
    # 1. Limpiar espacios del sensor_id
    sensor_id = registro_raw.get("sensor_id", "").strip()
    
    # 2. Extraer valor numérico de la temperatura eliminando unidades y espacios
    temp_raw = str(registro_raw.get("temperatura", "0"))
    temp_limpia = "".join(c for c in temp_raw if c.isdigit() or c in ".-")
    
    try:
        temperatura = float(temp_limpia)
    except ValueError:
        temperatura = 0.0
        
    # 3. Asegurar ubicación por defecto si viene vacía o ausente
    ubicacion = registro_raw.get("ubicacion")
    if not ubicacion or not ubicacion.strip():
        ubicacion = "Planta Desconocida"
    else:
        ubicacion = ubicacion.strip()
        
    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }


def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    """
    Toma la lista de sensores limpios y un umbral. Retorna una tupla:
    (lista_sensores_alerta, promedio_temperatura)
    """
    if not lista_sensores_limpios:
        return [], 0.0
        
    sensores_alerta = []
    suma_temperaturas = 0.0
    
    for sensor in lista_sensores_limpios:
        temp = sensor["temperatura"]
        suma_temperaturas += temp
        
        if temp > umbral_temperatura:
            sensores_alerta.append(sensor["sensor_id"])
            
    promedio_temperatura = suma_temperaturas / len(lista_sensores_limpios)
    return sensores_alerta, promedio_temperatura


if __name__ == "__main__":
    # Bloque de ejecución que demuestra el flujo completo
    datos_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002", "temperatura": "31.2 °C", "ubicacion": ""},
        {"sensor_id": " SENSOR-003", "temperatura": "19.8", "ubicacion": "Planta Sur "},
        {"sensor_id": "SENSOR-004", "temperatura": "28.0C", "ubicacion": "Planta Oeste"}
    ]
    
    print("--- FLUJO COMPLETO EJERCICIO 1 ---")
    # Limpieza de registros
    registros_limpios = [limpiar_registro_sensor(r) for r in datos_crudos]
    print("Registros limpios obtenidos:", registros_limpios)
    
    # Generación de resumen estadístico (umbral de 25.0 °C)
    umbral = 25.0
    alertas, promedio = generar_resumen_sensores(registros_limpios, umbral)
    
    print(f"\nReporte Consolidado:")
    print(f"- Umbral de temperatura: {umbral}°C")
    print(f"- Dispositivos en alerta: {alertas}")
    print(f"- Promedio térmico global: {promedio:.2f}°C")