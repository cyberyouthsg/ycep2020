const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
// const fs = require('fs')

var app = express();


app.use(bodyParser.urlencoded({extended: true}));
app.use('/', express.static(__dirname + '/public'));

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname + "/public/index.html"));
})

app.get('/secret', (req, res) => {
    res.sendFile(path.join(__dirname + "/public/secret.html"));
})

app.get('/admin', (req, res) => {
    res.sendFile(path.join(__dirname + "/public/secret.html"));
})

app.get('/nope', (req, res) => {
    res.sendFile(path.join(__dirname + "/public/secret.html"));
})

app.get('/cys', (req, res) => {
    res.sendFile(path.join(__dirname + "/public/secret.html"));
})

app.get('/test', (req, res) => {
    res.sendFile(path.join(__dirname + "/public/secret.html"));
})

app.get('/user', (req, res) => {
    res.sendFile(path.join(__dirname + "/public/flag.html"));
})

app.get('/more', (req, res) => {
    res.sendFile(path.join(__dirname + "/public/secret.html"));
})


app.get('/flag', (req, res) => {
    res.sendFile(path.join(__dirname + "/public/secret.html"));
})


app.listen(5000, () => {
    console.log("Server running on port 5000!");
})