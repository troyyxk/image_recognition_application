import React, { Component } from 'react';
import {useState} from 'react';
import '../fileUploader.css';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
toast.configure();

class FilerUploader extends Component {
    onInputChange = (e) => {
        // when submit new files, clear the records the old ones
        window.localStorage.clear();
        var set = new Set();
        for (let i = 0; i < e.target.files.length; i++) {
            if (window.localStorage.getItem(e.target.files[i].name) !== null) {
                toast.error('Cannot submit files with the same name!');
                window.localStorage.clear();
                return;
            }
            window.localStorage.setItem(e.target.files[i].name, "");
        }
        toast.success('Files have been successfully uploaded! Please turn to review tab for checking the result.');
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
                        <input type="file" onChange={this.onInputChange} class="form-control" multiple="true"/>
                    </div>
                </form>
            </div>
        );
    }
}

export default FilerUploader;