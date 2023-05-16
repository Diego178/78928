import './App.css';

import { BrowserRouter as Router, Route } from 'react-router-dom';
import { Routes } from 'react-router-dom';


import Temperatura from './pages/Temperatura';
import Calidad from './pages/Calidad';
import Navbar from './pages/Navbar';


function App() {
  
  return (
    <div className="App">
      <Router>
        <Navbar />
          <Routes>
            <Route path="/Temperatura" element={<Temperatura />} />
            <Route path="/Calidad" element={<Calidad />} />
            <Route path="*" element={<h1>Not Found</h1>} />
          </Routes>
      </Router>
    </div>
  );
}

export default App;
