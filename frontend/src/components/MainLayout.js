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
import { getProfile, logout, patchCard } from "../endpoints/api";
import { useEffect, useState } from "react";
import { useAuth } from "../contexts/useAuth";

const MainLayout = () => {
  const [profile, setProfile] = useState(null);
  const [incoming, setIncoming] = useState(null);
  const [accepting, setAccepting] = useState(false);
  const { myCrew } = useAuth();
  const navigator = useNavigate();

  useEffect(() => {
    const fetchProfile = async () => {
      const data = await getProfile();
      setProfile(data);
    };
    fetchProfile();
  }, []);

  useEffect(() => {
    const handler = (e) => {
      const payload = e.detail;
      setIncoming(payload);
    };
    window.addEventListener("incoming-call", handler);
    return () => window.removeEventListener("incoming-call", handler);
  }, []);

  const handleAccept = async () => {
    if (!incoming) return;
    setAccepting(true);
    try {
      await patchCard(incoming.card_id, {
        status: incoming.accept_next_status || "in_progress",
        datetime_data: {
          transmission_time: incoming.transmission_time,
          departure_time: new Date(),
        },
      });
      // Очищаем состояние входящего вызова, чтобы уведомление исчезло
      setIncoming(null);
      const nextUrl =
        incoming.detail_url ||
        incoming.detail_card ||
        `/cards/${incoming.card_id}/update`;
      navigator(nextUrl);
    } catch (error) {
      console.error("Ошибка при принятии вызова:", error);
      // В случае ошибки не очищаем состояние, чтобы пользователь мог попробовать снова
    } finally {
      setAccepting(false);
    }
  };

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
        {profile && (
          <Text mr={4}>
            Пользователь: {profile.full_name_display}
            {myCrew?.crew_number ? ` | Бригада №${myCrew.crew_number}` : ""}
          </Text>
        )}
        <Button colorScheme="red" onClick={handleLogout}>
          Logout
        </Button>
      </Flex>
      <Box p={8}>
        {profile?.role !== "dispatcher" && incoming && (
          <Box mb={4} p={4} borderWidth={1} borderRadius="md" bg="yellow.50">
            <HStack justifyContent="space-between">
              <Text>
                Новый вызов: карта №{incoming.card_id} —{" "}
                {incoming.address || "Адрес не указан"}
              </Text>
              <HStack spacing={2}>
                <Button
                  colorScheme="gray"
                  variant="outline"
                  onClick={() => setIncoming(null)}
                  isDisabled={accepting}
                >
                  Закрыть
                </Button>
                <Button
                  colorScheme="green"
                  onClick={handleAccept}
                  isLoading={accepting}
                >
                  Принять вызов
                </Button>
              </HStack>
            </HStack>
          </Box>
        )}
        <Outlet />
      </Box>
    </Box>
  );
};

export default MainLayout;
