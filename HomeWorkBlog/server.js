const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const app = express();
const PORT = 3000;

// Разрешаем CORS
app.use(cors());
app.use(express.json());

// Разрешаем все CORS запросы (можно настроить более строго)
app.use(cors());  // Это позволит всем доменам делать запросы к вашему серверу

app.use(express.json());


// Обработка POST запроса на сохранение комментариев
app.post('/save-comment', (req, res) => {
  const { name, email, comment } = req.body;
  const data = `Имя: ${name}\nEmail: ${email}\nКомментарий: ${comment}\n---\n`;

    // Сохраняем данные в файл
    const filePath = path.join(__dirname, 'comments.txt');
    fs.appendFile(filePath, data, (err) => {
        if (err) {
            console.error('Ошибка при сохранении комментария:', err);
            return res.status(500).send('Ошибка при сохранении комментария.');
        }
        res.status(200).send('Комментарий сохранен.');
    });
});

// Запуск сервера на порту 3000
app.listen(PORT, () => {
    console.log(`Сервер запущен на http://localhost:${PORT}`);
});
