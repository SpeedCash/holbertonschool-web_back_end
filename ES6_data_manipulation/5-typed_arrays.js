export default function createInt8TypedArray(length, position, value) {
  // Vérification des paramètres 'length' et 'position' pour s'assurer qu'ils sont valides
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  // Création d'un ArrayBuffer de la taille spécifiée
  const buffer = new ArrayBuffer(length);
  // Création d'une vue DataView pour manipuler le buffer
  const view = new DataView(buffer);

  // Mise à jour de la valeur à la position spécifiée
  view.setInt8(position, value);

  // Retourner la vue DataView
  return view;
}
