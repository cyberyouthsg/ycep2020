const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
// const fs = require('fs')

var app = express();

const TYPE_VALUE = "yes please type me into the input box!";
var startTime = 0;


app.use(bodyParser.urlencoded({extended: true}));
app.use('/', express.static(__dirname + '/public'));

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname + "/public/index.html"));
})

app.post("/start", (req, res) => {
    startTime = new Date();
    console.log("Time started!");
    // res.sendFile(path.join(__dirname + "/public/index.html"));
})

app.post('/', (req, res) => {
    var userInput = req.body.Input;

    if(userInput == TYPE_VALUE){
        var endTime = new Date();
        let elapsed = endTime - startTime;
        elapsed /= 1000;
        console.log(`${elapsed} seconds has passed..`);

        if(elapsed < 0.2){
            res.sendFile(path.join(__dirname + "/flag.html"));
        }else{
            res.sendFile(path.join(__dirname + "/public/slow.html"));
        }
    }else res.sendFile(path.join(__dirname + "/public/index.html"));
});


app.listen(5000, () => {
    console.log("Server running on port 5000!");
})