import React, { Component } from 'react';
import {useState} from 'react';
import '../fileUploader.css';

class FilerUploader extends Component {
    onInputChange = (e) => {
        console.log(e.target.files);
        console.log(e.target.files[0]);
        console.log(e.target.value);
    }

    onSubmit = (e) => {
        e.preventDefault();
    }

    render() {
        return(
            <div class="col-md-6">
                <form method="post" action="#" id="#" onSubmit={this.onSubmit}>
                    <div class="form-group files color">
                        <label>Upload Your File </label>
                        <input type="file" onChange={this.onInputChange} class="form-control" multiple=""/>
                    </div>
                </form>
            </div>
        );
    }
}

export default FilerUploader;