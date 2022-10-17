const express = require("express");
const PORT = process.env.PORT || 3000;
const app = express();

// app.get("/", (req, res) => res.send("Hello World!"));
app.use(express.static('public'))
app.post('/upload', upload.single('twitter_picture'), function (req, res, next) {

    child_process.execFile(
        "/usr/bin/convert",
        [path.join(__dirname, req.file.path), "-resize", "280x150", FILE_OUTPUT],
        function () {
            console.log('done resizing')
            return res.redirect('/public/result.html');
        }
    );
});
app.listen(PORT, () => console.log(`App listening on port ${PORT}!`));