import React, { useState, useEffect } from 'react'
import DropZone from './DropZone'
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import io from 'socket.io-client';

function InputField() {
    let navigate = useNavigate();
    let [email, setEmail] = useState('')
    let [dataUploaded, setDataUploaded] = useState(false);

    // Handles both the animations of the website and sending an email to the end user 
    let handleClick = async (event) => {
        document.getElementById('line').classList.add('sweep-left');
        document.getElementById('sweeper').classList.add('sweep-left');
        document.getElementById('about-section').classList.add('faded');

        event.preventDefault();

        // Sends the email to the provided email, currently a dummy email is sent, but either a JSON file 
        // of the data, or a link to a website visualizing the data was to be sent to the email provided in 
        // the input
        try {
            const response = await axios.post('/api/send-email', { email });
            console.log('Email sent successfully:', response.data);
        } catch (error) {
            console.error('Error sending email:', error);
        }

        // Timeout is here to allow animations to finish before changing tabs 
        setTimeout(() => {
            navigate('/loading')
        }, 1100)
    }

    let isValidEmail = (email) => {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // Checks for the file to finish loading so the user could press the upload button
    useEffect(() => {
        const socket = io('http://localhost:3000');

        socket.on('file-reassembled', (message) => {
            setDataUploaded(true)
        });

        return () => socket.disconnect();
    }, []);


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
                <button
                    className={`upload-button ${!dataUploaded || !isValidEmail(email) ? 'disabled' : ''}`}
                    onClick={handleClick}
                    disabled={!dataUploaded || !isValidEmail(email)}
                >
                    Upload
                </button>

            </div>
        </div>
    )
}

export default InputField