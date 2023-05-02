// App.js file to connect the front end to the backend file

import { useState } from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';


function StartButton({ setText }) {
  const onClick = () => { axios.get("http://127.0.0.1:8000/browse/dict")
.then((response) => {
const items = response.data.Data[0];
const stringItems = JSON.stringify(items);
setText(stringItems);
} )
.catch();
};
  return ( <button onClick={onClick}>Browse!</button>);
}

//function AestheticButton({ setText }) {
//  const onClick = () => { axios.get("http://127.0.0.1:8000/aesthetics_types/dict")
//.then((response) => {
//const items = response.data.Data[0];
// const stringItems = JSON.stringify(items);
// setText(stringItems);
// } )
// .catch();
// };
//   return ( <button onClick={onClick}>Click for aesthetic quiz!</button>);
//}


function App() {
const [text, setText] = useState('');
  return (
    <div className="App">
      <header className="App-header">
      <StartButton setText={setText} />
      {text}
      </header>
    </div>
  );
}

export default App;

//<AestheticButton setText={setText} /
