import React, { Component } from 'react';
import { Nav, Navbar, Container } from 'react-bootstrap'


class NavbarMain extends Component {
    // state = {}
    render() {
        return (
            <Navbar bg="dark" variant="dark">
                <Container>
                <Navbar.Brand href="#home">Image Recognization</Navbar.Brand>
                <Nav className="me-auto">
                    <Nav.Link href="#home">Home</Nav.Link>
                    <Nav.Link href="#features">Features</Nav.Link>
                    <Nav.Link href="#pricing">Pricing</Nav.Link>
                </Nav>
                </Container>
            </Navbar>
        );
    }
}

export default NavbarMain;