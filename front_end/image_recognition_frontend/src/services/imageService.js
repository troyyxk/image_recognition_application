import axios from 'axios';
import { ToastContainer, toast } from 'react-toastify';
import { config } from "../config.js";
import ResultTable from './../components/resultTable';
const {host, port} = config.backend;

export const postImage = (img, name) => {
    var json = JSON.stringify({ 'image_b64': img });
    axios.post("/api/upload/", json)
        .then((response) => {
            if (response.status === 200) {
                var irImage = [];
                var ogIrImage = JSON.parse(window.localStorage.getItem("irImage"));
                var i = 0;
                for (var key in Object.keys(ogIrImage)) {
                    if (ogIrImage[key].name === name) {
                        irImage.push({serialNum: ogIrImage[key].serialNum, name: ogIrImage[key].name, uuid: response.data.result.uuid, result: ogIrImage[key].status});
                    }
                    i++;
                }
                // console.log(irImage);
                window.localStorage.setItem("irImage", JSON.stringify(irImage));
            } else {
                toast.error('Upload image fail!');
                console.error("Upload image fail!");
                return false;
            }
            // console.log(response);
        })
        .catch((e) => {
            console.error("Error", e);
        })
    return true;
}

export const getResult = (uuid) => {
    // console.log("uuid")
    // console.log(uuid)
    var result = axios.get("/api/query/" + uuid + '/')
    return result;
}