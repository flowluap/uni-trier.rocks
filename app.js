const express = require('express'),
bodyParser = require('body-parser'),
path = require('path'),
http = require('http'),
crypto = require('crypto'),
helmet = require('helmet'),
exec = require('child_process').exec;

require('dotenv').config()

function verifyPostData(req, res, next) {
  const payload = JSON.stringify(req.body)
  if (!payload) {
    res.sendStatus(405);
    return next('Request body empty')
  }

  const hmac = crypto.createHmac('sha1', process.env.GIT_SECRET)
  const digest = 'sha1=' + hmac.update(payload).digest('hex')

  if (digest === req.headers['x-hub-signature']) {
    return next()
  }else{
    res.sendStatus(405);
  }
}


//configure express
const app = express();
const httpapp = express();

app.set('view engine', 'ejs');

app.use(bodyParser.json({limit: '50mb', extended: true}));
app.use(bodyParser.urlencoded({limit: '50mb',extended: true}));

app.use(helmet());

//routes with session
var ind = require('./routes/indexroutes'),
flz = require('./routes/files');

//Update Server
app.post("/github/webhook",verifyPostData, function (req, res) {
    if (req.body.ref=="refs/heads/files"){
      console.log("Update incoming");
      exec('cd /home/deploy/uni-trier.rocks && ./deploy.sh', function(err, stdout, stderr){
          if (err) {
           console.error(err);
           res.send(500,err);
         }else{
          res.sendStatus(200);
        }
      });
    }
});

app.use('/', ind);
app.use('/dateien', flz);
app.use("/public", express.static(path.join(__dirname, 'public')));
app.use("/files",express.static(process.env.FILE_DIR));

//catchin unkaught errors
app.use(function(err, req, res, next) {
  console.error(err.stack);
  res.status(500);
  res.send("Ein Fehler ist aufgetreten!");
});

app.get('*',function (req, res){
  res.status(404);
  res.send("404 Get");
});

app.post('*', function (req, res){
  res.status(404);
  res.send("404 Post");
});

http.createServer(app).listen(3000);
