const express = require('express');
const userRoutes = require('./routes/userRoutes');
const path = require('path');

const app = express();

const PORT = 3000;

app.use(express.static(path.join(__dirname, 'public')));

app.use(express.json());
app.use('/users', userRoutes);

app.get('/', (req, res) => {
    res.send('Hello Woooooorld');
});

app.get('/users/:userId/books/:bookId', (req, res) => {
    console.log(req.params);
    const { userId, bookId } = req.params
    console.log(userId);
    console.log(bookId);
    res.send(req.params);
});

app.listen(PORT, () => {
    console.log(`Servidor Node.js está funcionando na porta: ${PORT}`);
});
