function validatePasswords() {
  // Получаем значения паролей
  const password = document.getElementById('password').value;
  const confirmPassword = document.getElementById('confirm-password').value;

  // Получаем элемент для отображения ошибки
  const passwordErrorElement = document.getElementById('password-error');
  const nameErrorElement = document.getElementById('name-error');
  
  // Проверка совпадения паролей
  if (password !== confirmPassword) {
    passwordErrorElement.style.display = 'block';
    return false; // Отменяем отправку формы
  } else {
    passwordErrorElement.style.display = 'none';
  }

  // Проверка на корректность имени и фамилии
  const firstName = document.getElementById('first-name').value;
  const lastName = document.getElementById('last-name').value;

  const namePattern = /^[A-Za-zА-Яа-яЁё]+$/; // Регулярное выражение для проверки букв

  if (!namePattern.test(firstName) || !namePattern.test(lastName)) {
    nameErrorElement.style.display = 'block';
    return false; // Отменяем отправку формы
  } else {
    nameErrorElement.style.display = 'none';
  }

  return true; // Разрешаем отправку формы
}
