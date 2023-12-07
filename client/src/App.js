import './App.css';
import Welcome from './components/Welcome';
import Loading from './components/Loading';
import Header from './components/Header';
import { Routes, Route } from 'react-router-dom'

function App() {
  return (
    <div className="App">
      <Header />
      <Routes>
        <Route path='/' element={<Welcome />} />
        <Route path='/loading' element={<Loading />} />
      </Routes>
    </div>
  );
}

export default App;
