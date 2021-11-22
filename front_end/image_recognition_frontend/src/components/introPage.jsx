import logo from '../img/logo.png';

function IntroPage() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Group Project of CS655, Fall 2021, at Boston University.
        </p>
        <p>
          By 
          <a
            className="App-link"
            href="https://github.com/troyyxk"
            target="_blank"
            rel="noopener noreferrer"
          >
            Xingkun Yin
          </a>, 
          <a
            className="App-link"
            href="https://github.com/youyi1996"
            target="_blank"
            rel="noopener noreferrer"
          >
            Yi You
          </a>, 
          <a
            className="App-link"
            href="https://github.com/SuJingyu111"
            target="_blank"
            rel="noopener noreferrer"
          >
            Jingyu Su
          </a>, 
          <a
            className="App-link"
            href="https://github.com/wenyi999"
            target="_blank"
            rel="noopener noreferrer"
          >
            Boyi Song
          </a>
        </p>
        <p>
          Follow MIT Liscence.
        </p>
        <h5>
          Inmatural product, use at own risk.
        </h5>
      </header>
    </div>
  );
}

export default IntroPage;
