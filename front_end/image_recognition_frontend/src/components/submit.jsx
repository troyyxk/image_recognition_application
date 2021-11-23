import React, { Component } from 'react';
import '../App.css';
import FilerUploader from './fileUploader';

class Submit extends Component {
    // state = {}
    render() {
        return (
            <div className="App-header">
                <h1>Upload Your File </h1>
                <FilerUploader />
            </div>
        );
    }
}

export default Submit;