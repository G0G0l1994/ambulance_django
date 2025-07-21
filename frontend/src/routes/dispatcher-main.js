import { useState, useEffect } from "react";
import { VStack, Heading, Button } from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";
import { Text } from "@chakra-ui/react";
import { getProfile } from "../endpoints/api";
import { logout } from "../endpoints/api";

const DispatcherMain = () => {
    const navigator = useNavigate();
    const [profile, setProfile] = useState(null);
    useEffect(() => {
        const fetchProfile = async () => {
            const data = await getProfile();
            setProfile(data);
        };
        fetchProfile();
    }, []);
    const handleLogout = async () => {
        const success = await logout();
        if (success) {
            navigator("/login");
        }
    };
    const handleSubmit = async () => {
        navigator("/cards/create");
    };
    return (
        <VStack>
            <Heading> Диспетчерская </Heading>
            <Text>{profile?.username}! </Text>
            <VStack>
                <Button onClick={handleLogout} colorScheme="red">
                    Logout
                </Button>
                <Button onClick={handleSubmit} colorScheme="green">
                    Создать карту
                </Button>
            </VStack>
        </VStack>
    );
};

export default DispatcherMain;
