import React, { Component } from 'react';
import '../App.css';
import FilerUploader from './fileUploader';

class Main extends Component {
    // state = {}
    render() {
        return (
            <div className="App-header">
                <FilerUploader />
            </div>
        );
    }
}

export default Main;