export default function groceriesList() {
  // Création d'une nouvelle instance de Map
  const groceries = new Map();
  
  // Ajout des articles d'épicerie et de leurs quantités respectives dans la Map
  groceries.set('Apples', 10);
  groceries.set('Tomatoes', 10);
  groceries.set('Pasta', 1);
  groceries.set('Rice', 1);
  groceries.set('Banana', 5);
  
  // Retourner la Map contenant les articles d'épicerie
  return groceries;
}
