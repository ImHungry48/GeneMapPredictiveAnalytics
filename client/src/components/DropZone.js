import React, { useCallback, useState } from 'react';
import '../styles/Dropzone.css'

function DropZone() {
    let [dragging, setDragging] = useState(false);

    let handleDragIn = useCallback((e) => {
        e.preventDefault();
        e.stopPropagation();
    }, []);

    let handleDragOut = useCallback((e) => {
        e.preventDefault();
        e.stopPropagation();
        setDragging(false);
    }, []);

    let handleDragOver = useCallback((e) => {
        e.preventDefault();
        e.stopPropagation();

        if (e.dataTransfer.items && e.dataTransfer.items.length > 0) {
            setDragging(true);
        }
    }, []);

    let handleDrop = useCallback((e) => {
        e.preventDefault();
        e.stopPropagation();
        setDragging(false);

        // This function chunks up the file so it can be uploaded to the server
        if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
            let file = e.dataTransfer.files[0];
            uploadFileInChunks(file); 
            e.dataTransfer.clearData();
        }
    }, []);

    let CHUNK_SIZE = 5 * 1024 * 1024; 

    let uploadFileInChunks = async (file) => {
        let offset = 0;
        let chunkPromises = [];

        let uploadChunk = async (chunk, chunkNumber) => {
            let formData = new FormData();
            formData.append('file', new Blob([chunk]), file.name);
            formData.append('chunkNumber', chunkNumber);

            return fetch('/api/upload-chunk', {
                method: 'POST',
                body: formData,
            });
        };

        while (offset < file.size) {
            let chunk = file.slice(offset, offset + CHUNK_SIZE);
            chunkPromises.push(uploadChunk(chunk, offset / CHUNK_SIZE));
            offset += CHUNK_SIZE;
        }

        // Wait for all chunks to be uploaded
        await Promise.all(chunkPromises);

        // After all chunks are uploaded, call the reassemble endpoint
        fetch('/api/reassemble-file/chunk', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ filename: 'chunk' }) // Or any other data if needed
        })
            .then(response => response.text())
            .then(result => console.log(result))
            .catch(error => console.error('Error:', error));
    };


    return (
        <div
            className={`dropzone ${dragging ? 'active' : ''}`}
            onDrop={handleDrop}
            onDragOver={handleDragOver}
            onDragEnter={handleDragIn}
            onDragLeave={handleDragOut}
        >
            {dragging ?
                <div className="drop-message">Drop the files here ...</div> :
                <div className="drop-message">Drop genome here</div>
            }
        </div>
    );
};

export default DropZone;
