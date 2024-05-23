export default function updateStudentGradeByCity(students, city, newGrades) {
  // Vérification des arguments 'students' et 'newGrades' pour s'assurer qu'ils sont des tableaux
  if (!Array.isArray(students) || !Array.isArray(newGrades)) {
    throw new TypeError('The arguments students and newGrades must be arrays');
  }

  // Filtrer les étudiants par la ville spécifiée et mettre à jour leurs notes
  return students
    .filter(student => student.location === city)
    .map(student => {
      const gradeObj = newGrades.find(grade => grade.studentId === student.id);
      return { ...student, grade: gradeObj ? gradeObj.grade : 'N/A' };
    });
}
