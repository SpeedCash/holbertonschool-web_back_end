export default function updateUniqueItems(map) {
  // Vérification plus concise de l'instance de Map
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }

  // Utilisation de forEach pour une meilleure lisibilité
  map.forEach((value, key) => {
    if (value === 1) {
      map.set(key, 100);
    }
  });
}
