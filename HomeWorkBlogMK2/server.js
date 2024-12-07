const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

// Создаём папку для комментариев, если её нет
const commentsDir = path.join(__dirname, 'comments');
if (!fs.existsSync(commentsDir)) {
  fs.mkdirSync(commentsDir);
}

// Маршрут для сохранения комментария
app.post('/save-comment', (req, res) => {
  const { name, email, comment } = req.body;

  if (!name || !email || !comment) {
    return res.status(400).send('Все поля обязательны для заполнения.');
  }

  const timestamp = new Date().toISOString().replace(/:/g, '-');
  const filename = `${timestamp}_${name.replace(/ /g, '_')}.txt`;
  const filePath = path.join(commentsDir, filename);

  const data = `Имя: ${name}\nEmail: ${email}\nКомментарий: ${comment}\n---\n`;

  fs.writeFile(filePath, data, (err) => {
    if (err) {
      console.error('Ошибка при сохранении комментария:', err);
      return res.status(500).send('Ошибка при сохранении комментария.');
    }
    res.status(200).send('Комментарий сохранён.');
  });
});

// Запуск сервера
app.listen(PORT, () => {
  console.log(`Сервер запущен на http://localhost:${PORT}`);
});
