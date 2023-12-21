import React, { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import CssBaseline from '@mui/material/CssBaseline';


const OthersProfilePage = () => {
    const { username } = useParams();
    const [user, setUser] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchProfileData = async () => {
            try {
                const response = await fetch(`http://localhost:8000/profile/${username}`, { credentials: 'include' });
                //user is redirected to signin page if not authenticated
                if (response.status === 401) navigate('/signin');
                const data = await response.json();
                setUser(data);
            } catch (error) {
                //just redirecting user to their own profile page for now if user doesnt exist. to be changed later.
                navigate('/profile');
                console.error('Error fetching profile data:', error);
            }
        };

        fetchProfileData();
    }, [username, navigate]);

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
                {user && (
                    <>
                        <Typography variant="h3" sx={{ paddingBottom: '40px' }}>You are viewing {user.username}'s profile!</Typography>
                        <Typography variant="body1">Email: {user.email}</Typography>
                        <Typography variant="body1">TODO: Add friend button</Typography>
                        {/* other profile stuff here i guess */}
                    </>
                )}
            </Container>
        </>
    );
};

export default OthersProfilePage;
