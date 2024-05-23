export default function cleanSet(set, startString) {
  // Vérification des types d'arguments
  if (!(set instanceof Set)) {
    throw new TypeError('The first argument must be a Set');
  }
  if (typeof startString !== 'string' || startString.length === 0) {
    return '';
  }

  // Utilisation de 'map' et 'filter' pour une manipulation plus concise
  const result = Array.from(set)
    .filter(value => value.startsWith(startString))
    .map(value => value.slice(startString.length))
    .join('-');

  return result;
}
