export default function hasValuesFromArray(set, arr) {
  // Vérification des arguments 'set' et 'arr' pour s'assurer qu'ils sont de types corrects
  if (!(set instanceof Set)) {
    throw new TypeError('The first argument must be a Set');
  }
  if (!Array.isArray(arr)) {
    throw new TypeError('The second argument must be an array');
  }

  // Vérification si chaque valeur du tableau est présente dans le Set
  return arr.every(value => set.has(value));
}
