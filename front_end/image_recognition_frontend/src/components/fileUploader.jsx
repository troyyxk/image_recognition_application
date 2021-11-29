import React, { Component } from 'react';
import {useState} from 'react';
import '../fileUploader.css';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
toast.configure();

// reference
// https://stackoverflow.com/questions/28918232/how-do-i-persist-a-es6-map-in-localstorage-or-elsewhere

class FilerUploader extends Component {
    onInputChange = (e) => {
        // when submit new files, clear the records the old ones
        if (window.localStorage.getItem("irImage") !== null) {
            window.localStorage.removeItem("irImage");
        }
        var irImage = [];
        var nameSet = new Set();
        for (let i = 0; i < e.target.files.length; i++) {
            if (nameSet.has(e.target.files[i].name)) {
                toast.error('Cannot submit files with the same name!');
                window.localStorage.removeItem("irImage");
                return;
            }
            nameSet.add(e.target.files[i].name);
            irImage.push({name: e.target.files[i].name, uuid: "", result: ""});
        }
        toast.success('Files have been successfully uploaded! Please turn to review tab for checking the result.');
        window.localStorage.setItem("irImage", JSON.stringify(irImage));
        console.log(window.localStorage);
    }

    onSubmit = (e) => {
        e.preventDefault();
        console.log("In onSubmit");
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