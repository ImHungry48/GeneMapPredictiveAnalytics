import React from 'react'
import DropZone from './DropZone'
import { useNavigate } from 'react-router-dom';

function InputField() {
    let navigate = useNavigate();

    let handleClick = () => {
        document.getElementById('line').classList.add('sweep-left');
        document.getElementById('sweeper').classList.add('sweep-left');
        document.getElementById('about-section').classList.add('faded')
        setTimeout(() => {
            navigate('/loading')
        }, 1100)
    }

    return (
        <div class="input-field">
            <div class="title">Upload Genome Below</div>
            <DropZone />
            <div>
                <button class="upload-button" onClick={handleClick}>Upload</button>
            </div>
        </div>
    )
}

export default InputField