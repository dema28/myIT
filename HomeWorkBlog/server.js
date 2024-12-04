const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());
app.use(cors());  
app.use(express.json());

app.post('/save-comment', (req, res) => {
  const { name, email, comment } = req.body;
  const data = `Имя: ${name}\nEmail: ${email}\nКомментарий: ${comment}\n---\n`;
    const filePath = path.join(__dirname, 'comments.txt');
    fs.appendFile(filePath, data, (err) => {
        if (err) {
            console.error('Ошибка при сохранении комментария:', err);
            return res.status(500).send('Ошибка при сохранении комментария.');
        }
        res.status(200).send('Комментарий сохранен.');
    });
});

app.listen(PORT, () => {
    console.log(`Сервер запущен на http://localhost:${PORT}`);
});
