import React, { Component } from 'react';
import { Table } from 'react-bootstrap';
import '../App.css';

class ResultTable extends Component {
    // state = {}
    render() {
        return (
            <div className="App-header">
                <Table striped bordered hover variant="dark">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Image Name</th>
                            <th>Predicted Result</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>1</td>
                            <td>Mark</td>
                            <td>Otto</td>
                        </tr>
                        <tr>
                            <td>2</td>
                            <td>Jacob</td>
                            <td>Thornton</td>
                        </tr>
                        <tr>
                            <td>3</td>
                            <td colSpan="2">Larry the Bird</td>
                        </tr>
                    </tbody>
                </Table>
            </div>
        );
    }
}

export default ResultTable;