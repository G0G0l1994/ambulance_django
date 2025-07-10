import { VStack, Heading, Button } from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";
import { logout } from "../endpoints/api";

const MainPage = () => {
  const navigator = useNavigate();
  const handleLogout = async () => {
    const success = await logout();
    if (success) {
      navigator("/login");
    }
  };
  return (
    <VStack>
      <Heading> Welcome back User! </Heading>
      <VStack>
        <Button onClick={handleLogout} colorScheme="red">
          Logout
        </Button>
      </VStack>
    </VStack>
  );
};

export default MainPage;
