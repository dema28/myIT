document.querySelector('form').addEventListener('submit', async (e) => {
  e.preventDefault(); // Предотвращаем стандартное поведение формы

  const name = document.querySelector('#name').value.trim();
  const email = document.querySelector('#email').value.trim();
  const comment = document.querySelector('#comment').value.trim();

  if (name && email && comment) {
      // Отправляем данные на сервер для сохранения
      await fetch('http://localhost:3000/save-comment', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ name, email, comment }),
      });

      alert('Комментарий сохранен!');
      document.querySelector('form').reset(); // Сбрасываем форму
  } else {
      alert('Пожалуйста, заполните все поля!');
  }
});
