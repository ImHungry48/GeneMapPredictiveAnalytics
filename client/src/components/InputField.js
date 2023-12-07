import React, { useState } from 'react'
import DropZone from './DropZone'
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

function InputField() {
    let navigate = useNavigate();
    let [email, setEmail] = useState('')

    let handleClick = async (event) => {
        document.getElementById('line').classList.add('sweep-left');
        document.getElementById('sweeper').classList.add('sweep-left');
        document.getElementById('about-section').classList.add('faded');

        event.preventDefault();
        try {
            const response = await axios.post('/api/send-email', { email });
            console.log('Email sent successfully:', response.data);
        } catch (error) {
            console.error('Error sending email:', error);
        }

        setTimeout(() => {
            navigate('/loading')
        }, 1100)
    }

    return (
        <div class="input-field">
            <div class="title">Email</div>
            <input
                type="email"
                value={email}
                placeholder="Enter email"
                class="email-input"
                onChange={(e) => setEmail(e.target.value)}
            />
            <div class="title">Upload Genome Below</div>
            <DropZone />
            <div>
                <button class="upload-button" onClick={handleClick}>Upload</button>
            </div>
        </div>
    )
}

export default InputField