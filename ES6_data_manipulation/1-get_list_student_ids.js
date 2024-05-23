export default function getListStudentIds(students) {
  // Vérification plus concise de la validité de l'argument
  return Array.isArray(students) ? students.map(student => student.id) : [];
}
