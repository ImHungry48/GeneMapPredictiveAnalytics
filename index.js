let express = require('express');
let nodemailer = require('nodemailer')
let path = require('path');
let multer = require('multer');
let fs = require('fs');
let upload = multer({ dest: 'uploads/' });
let app = express();

let server = require('http').createServer(app);
let io = require('socket.io')(server);

app.use(express.static(path.join(__dirname, 'client/build')));
app.use(express.json());

// Sets up the agent that will send an email. Email service utilized is from SendGrid
let transporter = nodemailer.createTransport({
    service: 'sendgrid', 
    auth: {
        user: 'apikey',
        pass: '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' 
    }
});

// API route that sends an email to the end user
app.post('/api/send-email', (req, res) => {
    let { email } = req.body;

    let mailOptions = {
        from: 'insightsog@gmail.com', 
        to: email, 
        subject: 'Test email from code',
        text: 'Sup'
    };

    transporter.sendMail(mailOptions, function (error, info) {
        if (error) {
            console.log(error);
            res.status(500).send('Error sending email');
        } else {
            console.log('Email sent: ' + info.response);
            res.status(200).send('Email sent');
        }
    });
});

// Since the genome would be too large to upload in one go, the upload was seperated into 
// chunks and loaded into a folder (/client/uploads)
app.post('/api/upload-chunk', upload.single('file'), (req, res) => {
    let chunkNumber = req.body.chunkNumber;
    let file = req.file;

    let newPath = `${file.destination}/chunk-${chunkNumber}`;
    fs.renameSync(file.path, newPath);

    res.send({ message: 'Chunk received' });
});


// This code reassembles the chunks into a final file that is stored in the /client/final_upload folder
app.post('/api/reassemble-file/:filename', (req, res) => {
    let filename = req.params.filename;
    let chunksFolder = './uploads/';
    let finalPath = `./final_upload/${filename}`;

    let chunkNumber = 0;
    let fileStreams = [];

    // Checks to see if the chunks folder exists and starts stacking the chunks onto the filestream
    while (fs.existsSync(`${chunksFolder}chunk-${chunkNumber}`)) {
        let chunkPath = `${chunksFolder}chunk-${chunkNumber}`;
        fileStreams.push(fs.createReadStream(chunkPath));
        chunkNumber++;
    }

    // Begins combining the chunked file uploads into the final file 
    let finalStream = fs.createWriteStream(finalPath);

    let pipeNextStream = (chunkNumber) => {
        let chunkPath = `${chunksFolder}chunk-${chunkNumber}`;
        if (fs.existsSync(chunkPath)) {
            let readStream = fs.createReadStream(chunkPath);
            readStream.pipe(finalStream, { end: false });
            readStream.on('end', () => {
                fs.unlinkSync(chunkPath);  
                pipeNextStream(chunkNumber + 1);  
            });
        } else {
            finalStream.end();  
        }
    }

    // We start the stream at the first chunk (index 0)
    pipeNextStream(0);  

    // When the data is finished uploaded, a signal is sent to the front-end in order to enable the upload button
    finalStream.on('finish', () => {
        io.emit('file-reassembled')
        res.send('File reassembled successfully');
    });

});


// Renders the default webpage
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'client/build/index.html'));
});

let port = process.env.PORT || 3000;
server.listen(port);

console.log(`Express server listening on port ${port}`);
