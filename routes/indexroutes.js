var express = require('express'),
router = express.Router(),
path = require("path"),
ejs = require("ejs"),
fs = require("fs");

const ev = [{'day':'Tuesday','task':'Mathe Lehramt Abgabe Übung','note':'Abgabe bis 8:10 Campus I','prio':'high'},
            {'day':'Monday','task':'DSL Abgabe Übung','note':'Abgabe bis 10 Uhr Campus II','prio':'high'},
            {'day':'Wednesday','task':'Programmierung 1 Abgabe Übung','note':'','prio':'low'},
            {'day':'Sunday','task':'Rechnerstrukturen Abgabe Übung','note':'Abgabe nur alle zwei Wochen','prio':'low'}
          ]
const monthNames = ["JAN", "FEB", "MAR", "APR", "MAR", "JUN","JUL", "AUG", "SEP", "OCT", "NOV", "DEC"];
const weekNames = days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];



//get routes
router.get('/', function (req, res) {
  var date = new Date();
  var events = []
  for (var i=0;i<7;i++){
    date.setDate(date.getDate() + 1);
    for (j in ev){
      if (ev[j].day == weekNames[date.getDay()]){
        events.push({'date':date.getUTCDate(),
                     'day':weekNames[date.getDay()],
                     'month':monthNames[date.getMonth()],
                     'event':ev[j]});
      }
    }
  }
  res.render("index",{'events':events});
});

router.get('/impressum', function (req, res) {
  res.render("impressum");
});

//export router
module.exports = router;
