import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

const ProfilePage = () => {
    const [user, setUser] = useState({});
    const navigate = useNavigate();

    useEffect(() => {
        const fetchProfileData = async () => {
            try {
                const response = await fetch('http://localhost:8000/profile', { credentials: 'include' });
                //user is redirected to signin page if not authenticated
                if (response.status === 401) navigate('/signin');
                const data = await response.json();
                setUser(data);
            } catch (error) {
                console.error('Error fetching profile data:', error);
            }
        };

        fetchProfileData();
    }, []);

    return (
        <div>
            <h1>Welcome, {user.username}!</h1>
            <p>Email: {user.email}</p>
            <p>Muahahaha finally it works</p>
            {/* Render other profile information */}
        </div>
    );
};

export default ProfilePage;
