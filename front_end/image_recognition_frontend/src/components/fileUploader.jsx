import React, { Component } from 'react';
import {useState} from 'react';
import '../fileUploader.css';

class FilerUploader extends Component {
    onInputChange = (e) => {
        // when submit new files, clear the records the old ones
        window.localStorage.clear();
        for (let i = 0; i < e.target.files.length; i++) {
            window.localStorage.setItem(e.target.files[i].name, "");
        }
        console.log(e.target.files);
        console.log(e.target.files[0]);
        console.log(e.target.value);
        // window.localStorage.setItem();
        console.log(window.localStorage);
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
                        <input type="file" onChange={this.onInputChange} class="form-control" multiple="true"/>
                    </div>
                </form>
            </div>
        );
    }
}

export default FilerUploader;