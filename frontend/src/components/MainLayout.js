import {
  Box,
  Flex,
  Spacer,
  Button,
  Text,
  Hstack,
  HStack,
} from "@chakra-ui/react";
import { Link, Outlet, useNavigate } from "react-router-dom";
import { getProfile, login, logout } from "../endpoints/api";
import { useEffect, useState } from "react";

const MainLayout = () => {
  const [profile, setProfile] = useState(null);
  const navigator = useNavigate();

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

  return (
    <Box minH="100vh" bg="gray.50">
      <Flex as="nav" bg="blue.600" color="white" p={4} align="center">
        <Text fontWeight="bold" fontSize="xl">
          Ambulance
        </Text>
        <HStack spacing={4} ml={8}>
          {profile?.role === "dispatcher" ? (
            <Link to="/dispatcher-main">
              <Button colorScheme="blue" variant="solid">
                Главная
              </Button>
            </Link>
          ) : (
            <Link to="/">
              <Button colorScheme="blue" variant="solid">
                Главная
              </Button>
            </Link>
          )}
          {profile?.role === "doctor" && (
            <Link to={`/history/${profile.id}`}>
              <Button colorScheme="blue" variant="solid">
                Мои карты
              </Button>
            </Link>
          )}

          {profile?.role === "dispatcher" && (
            <>
              <Link to="/cards/create/">
                <Button colorScheme="purple" variant="solid">
                  Создать карту
                </Button>
              </Link>
              <Link to="/crew/list/">
                <Button colorScheme="green" variant="solid">
                  Бригады
                </Button>
              </Link>
            </>
          )}
        </HStack>
        <Spacer />
        {profile && <Text mr={4}>Пользователь: {profile.username}</Text>}
        <Button colorScheme="red" onClick={handleLogout}>
          Logout
        </Button>
      </Flex>
      <Box p={8}>
        <Outlet />
      </Box>
    </Box>
  );
};

export default MainLayout;
