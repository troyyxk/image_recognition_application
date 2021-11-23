import React, { Component } from 'react';
import {useState} from 'react';
import '../fileUploader.css';

export const FilerUploader = ({}) => {
    const [file, setFile] = useState(null);

    const onInputChange = (e) => {
        console.log(e.target.files);
        console.log(e.target.files[0]);
        setFile(e.target.files[0]);
        console.log(e.target.value);
    }
    
    const onSubmit = (e) => {
        e.preventDefault();
    }

    // state = {}
    return(
        <div class="col-md-6">
            <form method="post" action="#" id="#" onSubmit={onSubmit}>
                <div class="form-group files color">
                    <label>Upload Your File </label>
                    <input type="file" onChange={onInputChange} class="form-control" multiple=""/>
                </div>
            </form>
        </div>
    );
}

export default FilerUploader;