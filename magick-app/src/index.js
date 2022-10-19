const express = require('express')
const multer = require('multer')
const path = require('path')
const fs = require("fs");
const child_process = require("child_process");

const PORT = process.env.PORT || 3000;

const upload = multer({ dest: 'src/public/images' })
const app = express();

const FILE_OUTPUT = "src/public/images"
app.use(express.static('src/public'))
app.post('/upload', upload.single('picture'), function (req, res, next) {
    console.log(req.file)
    child_process.execFile(
        "/usr/bin/convert",
        [req.file.path, req.file.path + ".png"],
        function (error) {
            console.log('done resizing')
            console.log(error)
            return res.end(JSON.stringify({ picture: (path.join('images/', req.file.filename + ".png")) }));
        }
    );
    console.log(__dirname)
});
app.listen(PORT, () => console.log(`App listening on port ${PORT}!`));