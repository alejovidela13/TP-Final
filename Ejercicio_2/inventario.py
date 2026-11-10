# ejercicio_2/inventario.py
import json

class StockInvalidoError(Exception):
    """Excepción personalizada para impedir stock negativo."""
    pass


class DispositivoEcológico:
    def __init__(self, nombre, stock, costo):
        self.nombre = nombre
        self._stock = 0
        self.set_stock(stock) # Aplica encapsulamiento y validación
        self.costo = costo

    @property
    def stock(self):
        return self._stock

    def set_stock(self, valor):
        if valor < 0:
            raise StockInvalidoError(f"Error de stock: '{valor}'. El inventario no puede ser negativo.")
        self._stock = valor

    def ficha_tecnica(self):
        return f"Dispositivo: {self.nombre} | Stock: {self._stock} | Costo: ${self.costo}"

    def to_dict(self):
        return {
            "tipo": "DispositivoEcológico",
            "nombre": self.nombre,
            "stock": self._stock,
            "costo": self.costo
        }


class PanelSolar(DispositivoEcológico):
    def __init__(self, nombre, stock, costo, potencia_w, tipo_celda):
        super().__init__(nombre, stock, costo)
        self.potencia_w = potencia_w
        self.tipo_celda = tipo_celda

    # Polimorfismo aplicado a la ficha técnica
    def ficha_tecnica(self):
        return (f"[Panel Solar] {self.nombre} - Potencia: {self.potencia_w}W "
                f"({self.tipo_celda}) | Stock: {self.stock} | Costo: ${self.costo}")

    def to_dict(self):
        d = super().to_dict()
        d.update({
            "tipo": "PanelSolar",
            "potencia_w": self.potencia_w,
            "tipo_celda": self.tipo_celda
        })
        return d


class GestorInventario:
    @staticmethod
    def guardar_catalogo_json(lista_dispositivos, ruta_archivo):
        datos = [d.to_dict() for d in lista_dispositivos]
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print(f"Catálogo serializado y guardado exitosamente en '{ruta_archivo}'.")


if __name__ == "__main__":
    print("--- PRUEBAS DE INVENTARIO Y EXCEPCIONES ---")
    
    # 1. Verificación de captura controlada de StockInvalidoError
    try:
        print("Intentando crear un Panel Solar con stock negativo (-5)...")
        PanelSolar("Panel Test", -5, 100000, 300, "Policristalino")
    except StockInvalidoError as e:
        print(f"Excepción capturada correctamente: {e}\n")

    # 2. Creación de productos válidos y prueba de polimorfismo
    dispositivos_validos = []
    try:
        p1 = PanelSolar("Panel Monocristalino 450W", 20, 180000, 450, "Monocristalino")
        p2 = DispositivoEcológico("Termotanque Solar 200L", 5, 420000)
        
        dispositivos_validos.extend([p1, p2])
        
        print("Fichas técnicas comerciales:")
        for dispositivo in dispositivos_validos:
            print("-", dispositivo.ficha_tecnica())
            
    except StockInvalidoError as e:
        print(f"Error inesperado: {e}")

    print()
    # 3. Exportación exitosa al archivo JSON requerido
    GestorInventario.guardar_catalogo_json(dispositivos_validos, "catalogo_ecotech.json")