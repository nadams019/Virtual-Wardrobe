// App.js file to connect the front end to the backend file
//
import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import {
  BrowserRouter,
  Link,
  Route,
  Routes,
} from 'react-router-dom';

const API_BASE_URL = 'https://virtual-wardrobe.herokuapp.com';
const API_BROWSE_DICT_URL = `${API_BASE_URL}/browse/dict`;
// function StartButton({ setText }) {
//   const onClick = () => { axios.get("https://virtual-wardrobe.herokuapp.com/browse/dict")
// .then((response) => {
// const items = response.data.Data[0];
// const stringItems = JSON.stringify(items);
// setText(stringItems);
// } )
// .catch();
// };
//   return ( <button onClick={onClick}>Browse!</button>);
// }
async function fetchItems() {
  try {
    const onClick = () => {
      axios.get(API_BROWSE_DICT_URL).then((response) => {
        const items = response.data.Data[0];
        return items;
      });
    };
  } catch (error) {
    console.error(error);
    return null;
  }
}

// function BrowsePage({ items }) {
//   return (
//     <div>
//       {items.map((item) => (
//         <div key={item.id}>
//           <h2>{item.name}</h2>
//           <p>{item.description}</p>
//           <img src={item.image_url} alt={item.name} />
//         </div>
//       ))}
//     </div>
//   );
//}
function Homepage() {
return (
  <nav>
    <Link to="/browse">Browse</Link>
  </nav>
);
}
function Browse(){
  return(
      <h2> Browse</h2>
  );
}
function App() {
  const [items, setItems] = useState([]);

  async function loadItems() {
    const items = await fetchItems();
    if (items) {
      setItems(items);
    }
  }

  useEffect(() => {
    loadItems();
  }, []);

  return (
      <div className="App">
        <header className="App-header">
          <BrowserRouter>
          <Routes>
            <Route path="/browse" element={<Browse />} />
            <Route path="/" element={<Homepage />} />
          </Routes>
          </BrowserRouter>
        </header>
    </div>
  );
}



export default App;
//<BrowsePage items={items} />
// import { useState } from 'react';
// import axios from 'axios';
// import logo from './logo.svg';
// import './App.css';
//
//

//
// //function AestheticButton({ setText }) {
// //  const onClick = () => { axios.get("http://127.0.0.1:8000/aesthetics_types/dict")
// //.then((response) => {
// //const items = response.data.Data[0];
// // const stringItems = JSON.stringify(items);
// // setText(stringItems);
// // } )
// // .catch();
// // };
// //   return ( <button onClick={onClick}>Click for aesthetic quiz!</button>);
// //}
//
//
// function App() {
// const [text, setText] = useState('');
//   return (
//     <div className="App">
//       <header className="App-header">
//       <StartButton setText={setText} />
//       {text}
//       </header>
//     </div>
//   );
// }
//
// export default App;
//
// //<AestheticButton setText={setText} /
