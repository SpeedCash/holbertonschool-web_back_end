export default function setFromArray(arr) {
  // Vérification de l'argument 'arr' pour s'assurer qu'il s'agit d'un tableau
  if (!Array.isArray(arr)) {
    throw new TypeError('The argument must be an array');
  }

  // Création d'un Set à partir du tableau
  return new Set(arr);
}
