const mongoose = require('mongoose');

mongoose.connect('mongodb+srv://qtmoura:150296@cluster.tdovyaf.mongodb.net/', { useNewUrlParser: true, useUnifiedTopology: true });

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'Erro de conexão com o banco de dados:'));
db.once('open', () => {
    console.log('Conexão bem-sucedida com o banco de dados MongoDB!');
});

module.exports = db;
