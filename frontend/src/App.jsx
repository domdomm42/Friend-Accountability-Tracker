import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { SignupPage } from './pages/authentication/SignupPage';
import { SigninPage } from './pages/authentication/SigninPage';
import ProfilePage from './pages/social/ProfilePage';
import OthersProfilePage from './pages/social/OthersProfilePage';

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path='/signup' element={<SignupPage />} />
          <Route path='/signin' element={<SigninPage />} />
          <Route path='/profile' element={<ProfilePage />} />
          <Route path='/profile/:username' element={<OthersProfilePage />} />
          <Route path='*' element={<div>Route not found</div>} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
