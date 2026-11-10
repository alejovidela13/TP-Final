from django.shortcuts import render
from .utils import obtener_metricas_consumo

def vista_panel_sustentabilidad(request):
    """
    Procesa las métricas de consumo y prepara el contexto para renderizar
    la plantilla sustentabilidad/panel.html.
    """
    # Simulación de historial de consumos por planta industrial
    historial_registros = [
        {"planta": "Planta Norte", "consumo": 14500.0},
        {"planta": "Planta Sur", "consumo": 22100.5},
        {"planta": "Planta Este", "consumo": 9800.0}
    ]
    
    metricas = obtener_metricas_consumo(historial_registros)
    
    contexto = {
        "total_emisiones": metricas["total_emisiones"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "registros": historial_registros
    }
    
    return render(request, "sustentabilidad/panel.html", contexto)