# Sistema de Recomendación de Productos

Este proyecto implementa un sistema de recomendación de productos utilizando filtrado colaborativo basado en usuarios. El sistema analiza las calificaciones de los usuarios para generar recomendaciones personalizadas.

## Características

- Implementación de filtrado colaborativo usuario-usuario
- Cálculo de similitud entre usuarios usando similitud del coseno
- Generación de recomendaciones personalizadas basadas en calificaciones de usuarios similares
- Matriz de ejemplo incluida para demostración

## Requisitos

El sistema requiere las siguientes bibliotecas de Python:
- pandas
- numpy
- scikit-learn

Para instalar las dependencias, ejecute:
```bash
pip install pandas numpy scikit-learn
```

## Estructura del Código

El código principal se encuentra en `recommendation_system.py` y contiene:

### Clase RecommendationSystem

- `__init__()`: Inicializa el sistema con una matriz de ejemplo de calificaciones
- `get_user_similarity(user_id)`: Calcula la similitud entre un usuario y todos los demás
- `get_recommendations(user_id, n_recommendations)`: Genera recomendaciones para un usuario específico

## Uso

```python
# Crear una instancia del sistema
rs = RecommendationSystem()

# Obtener recomendaciones para un usuario específico
user_id = 'Usuario1'
recommendations = rs.get_recommendations(user_id)
```

## Funcionamiento

1. **Matriz de Calificaciones**: 
   - Filas: Usuarios
   - Columnas: Productos
   - Valores: Calificaciones (1-5) o 0 si no hay calificación

2. **Proceso de Recomendación**:
   - Calcula la similitud entre usuarios usando similitud del coseno
   - Identifica productos no calificados por el usuario objetivo
   - Genera predicciones basadas en calificaciones de usuarios similares
   - Ordena y devuelve las mejores recomendaciones

## Ejemplo de Salida

```
Recomendaciones para Usuario1:
Producto4: 4.20
Producto3: 3.85
Producto5: 3.50
```

## Limitaciones y Posibles Mejoras

- La matriz de calificaciones actual es un ejemplo y debería reemplazarse con datos reales
- Se podría implementar manejo de casos extremos (usuarios sin calificaciones, etc.)
- Posibilidad de añadir más métricas de similitud
- Implementar filtrado basado en elementos como alternativa

## Contribuciones

Siéntase libre de contribuir al proyecto mediante pull requests. Algunas áreas de mejora sugeridas:
- Implementación de más algoritmos de recomendación
- Optimización del rendimiento
- Añadir tests unitarios
- Mejorar la documentación

## Licencia

Este proyecto está disponible bajo la licencia MIT.