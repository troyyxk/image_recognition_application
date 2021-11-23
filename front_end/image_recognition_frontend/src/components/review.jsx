import React, { Component } from 'react';
import { Container,Row } from 'react-bootstrap';
import ResultTable from './resultTable';
import '../App.css';

class Review extends Component {
    // state = {}
    render() {
        return (
            <div className="App-header">
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