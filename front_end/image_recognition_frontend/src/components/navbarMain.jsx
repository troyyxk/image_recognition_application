import React, { Component } from 'react';
import { Nav, Navbar, Container } from 'react-bootstrap'


class NavbarMain extends Component {
    // state = {}
    render() {
        return (
            <Navbar bg="dark" variant="dark">
                <Container>
                <Navbar.Brand href="home">Image Recognization</Navbar.Brand>
                <Nav className="me-auto">
                    <Nav.Link href="home">Home</Nav.Link>
                    <Nav.Link href="start">Start</Nav.Link>
                    <Nav.Link href="documentation">Documentation</Nav.Link>
                </Nav>
                </Container>
            </Navbar>
        );
    }
}

export default NavbarMain;