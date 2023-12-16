import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import CssBaseline from '@mui/material/CssBaseline';


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
        <>
            <CssBaseline />
            <Box sx={{ flexGrow: 1}}>
                <AppBar position="absolute">
                    <Toolbar>
                    <IconButton
                        size="large"
                        edge="start"
                        color="inherit"
                        aria-label="menu"
                        sx={{ mr: 2 }}
                    >
                        <MenuIcon />
                    </IconButton>
                    <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>Profile</Typography>
                    <Button color="inherit">Logout</Button>
                    </Toolbar>
                </AppBar>
            </Box>
            <Container maxWidth="xl" sx={{ padding: '60px' }}> 
                <Typography variant="h3" sx={{ paddingBottom: '40px' }}>Welcome, {user.username}!</Typography>
                <Typography variant="body1">Email: {user.email}</Typography>
                <Typography variant="body1">Muahahaha finally it works</Typography>
                {/* other profile stuff here i guess */}
            </Container>
        </>
    );
};

export default ProfilePage;
