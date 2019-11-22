var express = require('express'),
bodyParser = require('body-parser'),
path = require('path'),
flash = require('connect-flash'),
session = require('express-session'),
passport = require('passport'),
db = require('./routes/db'),
pp = require('./passport'),
https = require('https'),
http = require('http'),
fs = require('fs'),
cookieParser = require('cookie-parser'),
nodemailer = require("nodemailer"),
TelegramBot = require('node-telegram-bot-api'),
helmet = require('helmet');



// Https certs
var options = {
    key: fs.readFileSync('/etc/letsencrypt/live/uni-trier.rocks/privkey.pem'),
    cert: fs.readFileSync('/etc/letsencrypt/live/uni-trier.rocks/fullchain.pem')
};


//configure express
const app = express();
const httpapp = express();

app.set('view engine', 'ejs');

app.use(bodyParser.json({limit: '50mb', extended: true}));
app.use(bodyParser.urlencoded({limit: '50mb',extended: true}));

app.use(helmet());

//routes with session
var ind = require('./routes/indexroutes'),
    adm = require('./routes/admin/routes');

app.use('/admin', adm);
app.use('/', ind);
app.use("/public", express.static(path.join(__dirname, 'public')));
app.use("/files",express.static('/root/remstorage/fileupload'));


//catchin unkaught errors
app.use(function(err, req, res, next) {
  console.error(err.stack);
  res.send("Ein Fehler ist aufgetreten!");
});

// redirect traffic
httpapp.get("*", function (req, res, next) {
    res.redirect(301,"https://" + req.headers.host + req.path);
});

app.get('*',function (req, res){
  res.status(404);
  res.send("404 Get");
});

app.post('*', function (req, res){
  res.status(404);
  res.send("404 Post");
});

// Create an HTTPS service identical to the HTTP service.
http.createServer(httpapp).listen(80);
https.createServer(options, app).listen(443);
