// Функция для проверки паролей
function validatePasswords() {
  const password = document.getElementById('password').value;
  const confirmPassword = document.getElementById('confirm-password').value;
  const firstName = document.getElementById('first-name').value;
  const lastName = document.getElementById('last-name').value;

  // Скрыть все сообщения об ошибках
  document.getElementById('password-error').style.display = 'none';
  document.getElementById('name-error').style.display = 'none';

  let isValid = true;

  // Проверка паролей на совпадение
  if (password !== confirmPassword) {
    document.getElementById('password-error').style.display = 'block';
    isValid = false;
  }

  // Проверка имени и фамилии на допустимые символы
  const namePattern = /^[A-Za-zА-Яа-яЁё]+$/;
  if (!namePattern.test(firstName) || !namePattern.test(lastName)) {
    document.getElementById('name-error').style.display = 'block';
    isValid = false;
  }

  // Возвращаем false, если есть ошибки, чтобы предотвратить отправку формы
  return isValid;
}
