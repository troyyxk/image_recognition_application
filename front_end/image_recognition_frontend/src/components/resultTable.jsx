import React, { Component, Fragment } from 'react';
import { Container,Row, Button, Table } from 'react-bootstrap';
import { ToastContainer, toast } from 'react-toastify';
import { getResult } from '../services/imageService';
import '../App.css';
import Submit from './submit';

class ResultTable extends Component {
    state = {}
    
    constructor() {
        super();
        var irImage = JSON.parse(window.localStorage.getItem("irImage"));
        this.state = {irImage: irImage};
    }

    handleOnClick = () => {
        for (var key in Object.keys(this.state.irImage)) {
            var uuid = this.state.irImage[key].uuid;
            var result = getResult(uuid);
            result
            .then((response) => {
                // console.log(response);
                if (response.status === 200) {
                    // console.log(response.data)
                    var status = response.data.result.status;
                    var result;
                    var irImage = [];
                    var ogIrImage = JSON.parse(window.localStorage.getItem("irImage"));
                    var i = 0;
                    for (var key in Object.keys(ogIrImage)) {
                        if (ogIrImage[key].uuid === uuid) {
                            if (status === 0) {
                                result = "Status: Waiting"
                            }
                            else if (status === 1) {
                                result = "Status: Running"
                            }
                            else if (status === 2) {
                                result = response.data.result.category;
                            }
                            else if (status === 3) {
                                result = "Status: Failed"
                            }
                        }
                        irImage.push({serialNum: ogIrImage[key].serialNum, name: ogIrImage[key].name, uuid: ogIrImage[key].uuid, result: result});
                        i++;
                    }
                    console.log("in getResult")
                    console.log(irImage);
                    window.localStorage.setItem("irImage", JSON.stringify(irImage));
                    this.setState({irImage: irImage});
                } else {
                    toast.error('Upload image fail!');
                    console.error("Upload image fail!");
                    return false;
                }
            })
            .catch((e) => {
                console.error("Error", e);
            })
        }
    }

    render() {
        if (window.localStorage.getItem("irImage") === null){
            return (
                <div className="App-header">
                    <h1> Not tasks right now, please submit tasks at the "Submit" tab </h1>
                </div>
                );
        }
        
        return (
            <div className="App-header">
                <Button variant="info" onClick={this.handleOnClick}>Refresh</Button>
                <Table striped bordered hover variant="dark">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Image Name</th>
                            <th>Predicted Result</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.state.irImage.map(item => (
                            <tr>
                                <td>{item.serialNum}</td>
                                <td>{item.name}</td>
                                <td>{item.result}</td>
                            </tr>
                        ))}
                    </tbody>
                </Table>
            </div>
        );
    }
}

export default ResultTable;