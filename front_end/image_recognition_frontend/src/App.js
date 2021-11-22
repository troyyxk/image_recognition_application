import './App.css';
import NavbarMain from './components/navbarMain';
import IntroPage from './components/introPage';
import Documentation from './components/documentation';
import Main from './components/Main';
import {BrowserRouter, Switch, Route} from 'react-router-dom';
// for the change to react router dom v6
// https://stackoverflow.com/questions/63124161/attempted-import-error-switch-is-not-exported-from-react-router-dom?rq=1

function App() {
  return (
    <div>
      <NavbarMain />
      <BrowserRouter>
          <Switch>
            {/* <Route exact path="/team/:id" component={Team} /> */}
            <Route extact path="/home" component={IntroPage} />
            <Route extact path="/documentation" component={Documentation} />
            <Route extact path="/start" component={Main} />
            <Route path="/" component={IntroPage} />
          </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
