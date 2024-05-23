export default function getStudentsByLocation(students, city) {
  // Vérification de l'argument 'students' pour s'assurer qu'il s'agit d'un tableau
  if (!Array.isArray(students)) {
    throw new TypeError('The first argument must be an array');
  }

  // Utilisation de la méthode 'filter' pour retourner les étudiants correspondant à la ville spécifiée
  return students.filter(student => student.location === city);
}
