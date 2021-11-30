import React, { Component } from 'react';
import {useState} from 'react';
import '../fileUploader.css';
import { ToastContainer, toast } from 'react-toastify';
import { postImage } from '../services/imageService';
import 'react-toastify/dist/ReactToastify.css';
toast.configure();

// reference
// https://stackoverflow.com/questions/28918232/how-do-i-persist-a-es6-map-in-localstorage-or-elsewhere

class  FilerUploader extends Component {

    state = { names: [], data : [] };

    onInputChange = (e) => {
        // when submit new files, clear the records the old ones
        if (window.localStorage.getItem("irImage") !== null) {
            window.localStorage.removeItem("irImage");
        }
        var irImage = [];
        var nameSet = new Set();
        var names = [];
        var curData = [];
        for (let i = 0; i < e.target.files.length; i++) {
            var curFile = e.target.files[i];
            var curName = curFile.name;
            if (nameSet.has(curName)) {
                toast.error('Cannot submit files with the same name!');
                return;
            }
            nameSet.add(curName);
            irImage.push({serialNum: i+1, name: curName, uuid: "", result: "Unknown"});
            names.push(curName);
            curData.push(curFile);
        }
        window.localStorage.setItem("irImage", JSON.stringify(irImage));
        this.setState({ names : names });
        this.setState({ data : curData });
    }

    onSubmit = (e) => {
        e.preventDefault();
        console.log("this.state")
        // console.log(this.state);
        var reader = new FileReader();
        for (var i = 0; i < this.state.data.length; i++) {
            var name = this.state.names[i];
            reader.onload = function () {
                var base64String = reader.result;
                console.log(name)  
                if (!postImage(base64String, name)) {
                    return;
                }
            }
            reader.readAsDataURL(this.state.data[i]);
        }
        toast.success('Files have been successfully uploaded! Please turn to review tab for checking the result.');
    }

    render() {
        return(
            <div class="col-md-6">
                <form method="post" action="#" id="#" onSubmit={this.onSubmit}>
                    <div class="form-group files color">
                        <input type="file" onChange={this.onInputChange} class="form-control" />
                    </div>
                    <button>Submit</button>
                </form>
            </div>
        );
    }
}

export default FilerUploader;