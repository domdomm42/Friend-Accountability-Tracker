import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { SignupPage } from './pages/authentication/SignupPage';

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path='/signup' element={<SignupPage />} />
          <Route path='*' element={<div>Route not found</div>} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
