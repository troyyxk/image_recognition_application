import React, { Component, Fragment } from 'react';
import { Container,Row, Button, Table } from 'react-bootstrap';
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
            getResult(uuid);
        }
        window.location.reload();
    }

    render() {
        if (window.localStorage.getItem("irImage") === null){
            return (
                <div className="App-header">
                    <h1> Not tasks right now, please submit tasks at the "Submit" tab </h1>
                </div>
                );
        }
        
        console.log(this.state.irImage)
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