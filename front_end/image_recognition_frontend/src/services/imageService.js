import axios from 'axios';
import { config } from "../config.js";
const {host, port} = config.backend;

export const postImage = (img) => {
    axios.post(host, image)
        .then((e) => {
            console.log('Success')
        })
        .catch((e) => {
            console.error("Error", e)
        })
}