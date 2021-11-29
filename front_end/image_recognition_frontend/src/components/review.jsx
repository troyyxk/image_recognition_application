import React, { Component } from 'react';
import { Container,Row, Button } from 'react-bootstrap';
import ResultTable from './resultTable';
import '../App.css';

class Review extends Component {
    // state = {}
    render() {
        return (
            <div className="App-header">
                <h1> Refersh Status: </h1>
                <Button variant="info">Refresh</Button>
                <Container fluid="md">
                    <Row>
                        <ResultTable/>
                    </Row>
                </Container>
            </div>
        );
    }
}

export default Review;