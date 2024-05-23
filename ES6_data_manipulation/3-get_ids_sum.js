export default function getStudentIdsSum(students) {
  // Vérification de l'argument 'students' pour s'assurer qu'il s'agit d'un tableau
  if (!Array.isArray(students)) {
    throw new TypeError('The argument must be an array');
  }

  // Utilisation de la méthode 'reduce' pour calculer la somme des 'id' des étudiants
  return students.reduce((sum, student) => sum + student.id, 0);
}
