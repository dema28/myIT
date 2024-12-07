document.querySelectorAll('form').forEach((form) => {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const name = form.querySelector('input[name="name"]').value.trim();
    const email = form.querySelector('input[name="email"]').value.trim();
    const comment = form.querySelector('textarea[name="comment"]').value.trim();

    if (name && email && comment) {
      try {
        const response = await fetch('http://localhost:3000/save-comment', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ name, email, comment }),
        });

        if (response.ok) {
          alert('Комментарий сохранён!');
          form.reset();
        } else {
          alert('Ошибка при сохранении комментария.');
        }
      } catch (error) {
        console.error('Ошибка:', error);
        alert('Ошибка подключения к серверу.');
      }
    } else {
      alert('Пожалуйста, заполните все поля!');
    }
  });
});
