import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class RecommendationSystem:
    def __init__(self):
        # Ejemplo de matriz de usuarios y productos (filas=usuarios, columnas=productos)
        # Los valores representan las calificaciones (1-5) o 0 si no hay calificación
        self.ratings_matrix = pd.DataFrame({
            'Producto1': [5, 3, 0, 1, 4],
            'Producto2': [4, 0, 0, 5, 3],
            'Producto3': [1, 2, 5, 4, 0],
            'Producto4': [0, 4, 2, 0, 3],
            'Producto5': [2, 4, 1, 3, 5]
        }, index=['Usuario1', 'Usuario2', 'Usuario3', 'Usuario4', 'Usuario5'])

    def get_user_similarity(self, user_id):
        """Calcula la similitud entre un usuario y todos los demás usuarios."""
        # Obtener el vector de calificaciones del usuario actual
        user_ratings = self.ratings_matrix.loc[user_id].values.reshape(1, -1)
        
        # Calcular similitud del coseno entre este usuario y todos los demás
        similarity_scores = cosine_similarity(user_ratings, self.ratings_matrix)
        return similarity_scores[0]

    def get_recommendations(self, user_id, n_recommendations=3):
        """Genera recomendaciones para un usuario específico."""
        # Obtener similitudes con otros usuarios
        user_similarities = self.get_user_similarity(user_id)
        
        # Crear un DataFrame con las similitudes
        similar_users = pd.Series(user_similarities, index=self.ratings_matrix.index)
        # Excluir al usuario actual
        similar_users = similar_users.drop(user_id)
        
        # Obtener los productos que el usuario aún no ha calificado
        user_ratings = self.ratings_matrix.loc[user_id]
        not_rated = user_ratings[user_ratings == 0].index
        
        # Calcular predicciones para productos no calificados
        recommendations = {}
        for product in not_rated:
            # Obtener calificaciones de otros usuarios para este producto
            product_ratings = self.ratings_matrix[product]
            # Calcular predicción ponderada
            weighted_sum = sum(similar_users * product_ratings)
            similarity_sum = sum(similar_users)
            if similarity_sum != 0:
                recommendations[product] = weighted_sum / similarity_sum
        
        # Ordenar y obtener las mejores recomendaciones
        recommendations = pd.Series(recommendations)
        recommendations = recommendations.sort_values(ascending=False)
        return recommendations.head(n_recommendations)

def main():
    # Crear instancia del sistema de recomendación
    rs = RecommendationSystem()
    
    # Ejemplo de uso
    user_id = 'Usuario1'
    recommendations = rs.get_recommendations(user_id)
    
    print(f"\nRecomendaciones para {user_id}:")
    for product, score in recommendations.items():
        print(f"{product}: {score:.2f}")

if __name__ == "__main__":
    main()
