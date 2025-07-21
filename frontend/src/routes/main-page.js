import { VStack, Heading, Button } from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";
import { logout, getProfile } from "../endpoints/api";
import { useEffect, useState } from "react";

const MainPage = () => {
    const navigator = useNavigate();
    const handleLogout = async () => {
        const success = await logout();
        if (success) {
            navigator("/login");
        }
    };
    const [profile, setProfile] = useState(null);
    useEffect(()=>{
        const fetchProfile = async () => {
            const data = await getProfile();
            setProfile(data);
        };
        fetchProfile()
    }, []);
    return (
        <VStack>
            <Heading> Welcome back { profile?.username }! </Heading>
            <VStack>
                <Button onClick={handleLogout} colorScheme="red">
                    Logout
                </Button>
            </VStack>
        </VStack>
    );
};

export default MainPage;
