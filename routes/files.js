var express = require('express'),
router = express.Router(),
path = require("path"),
ejs = require("ejs"),
fs = require("fs");

var docfolder = process.env.FILE_DIR;

const readdirSync = (p, a = []) => {
  if (fs.statSync(p).isDirectory())
    fs.readdirSync(p).map(f => readdirSync(a[a.push(path.join(p, f)) - 1], a))
  return a
}

stripPath = function(pfad){
  return path.normalize(pfad.replace("%2e","").replace("%2F"),"").replace(/^(\.\.(\/|\\|$))+/, '');
};


function whatContent(filePath, res){
  var folders = [];
  var filez = [];
  icons = {"txt":'far fa-file-alt',
          'pdf':"far fa-file-pdf",
          'mp4':"far fa-file-video",
          'mov':"far fa-file-video",
          'mp3':"far fa-file-audio",
          'wav':"far fa-file-audio",
          'flac':"far fa-file-audio",
          'zip':"far fa-file-archive",
          'csv':"fas fa-file-csv",
          'pptx':"far fa-file-powerpoint",
          'docx':"far fa-file-word",
          'png':"far fa-file-image",
          'jpg':"far fa-file-image",
          'gif':"far fa-file-image",
          'jpeg':"far fa-file-image",
          'xlsm':"far fa-file-excel"
        }

  const isFile = fileName => {
    return fs.lstatSync(fileName).isFile();
  }

  const isFolder = folderName => {
    return fs.lstatSync(folderName).isDirectory();
  }
  // try {
    fs.readdirSync(filePath).forEach(file => {

        if (isFile(path.join(filePath, file)) && file[0] != "."){
          filez.push({'name':file,'path':path.join(filePath, file),'icon':(file.split(".")[file.split(".").length-1] in icons ? icons[file.split(".")[file.split(".").length-1]] : "fas fa-file")});
        }

        if (isFolder(path.join(filePath, file)) && file[0] != "."){
            folders.push({'name':file,'path':path.join(filePath, file),'content':readdirSync(path.join(filePath, file))});
        }
    });
//  }
  // catch(err) {
  //   return "error";
  // }

  return [folders,filez];
}

function rmfilefrompath(path){
  var newpath="";
  const elm = path.split("/").slice(1,path.split("/").length-1);
  for (i in elm){
    if (i == elm.length -1){
      newpath +=elm[i]
    }else{
      newpath +=elm[i] +"/"
    }
  }
  return newpath;
}

router.get('/', function (req, res) {
    if (!req.query.path || req.query.path=="/"){
      var result = whatContent(docfolder);
      var pfad = "";
      var pb=""
    }else{
      var pfad = stripPath(req.query.path);
      var result = whatContent(path.join(docfolder,pfad));
      var pb = rmfilefrompath(pfad);
    }
    if (result != "error"){
      res.render('files', {title:"Explorer",
                           folders: result[0],
                           files:result[1],
                           path:pfad,
                           pathback:pb,
                         });
    }else{
      res.send("file not found");
    }
});

//export router
module.exports = router;
