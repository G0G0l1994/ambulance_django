import {
  VStack,
  Button,
  FormControl,
  FormLabel,
  FormHelperText,
  Input,
  Text,
} from "@chakra-ui/react";

import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../endpoints/api";
import { useAuth } from "../contexts/useAuth";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigation = useNavigate();
  const { refreshAuth } = useAuth();

  const handleLogin = async () => {
    const success = await login(username, password);

    if (success) {
      await refreshAuth();
      navigation("/");
    }
  };

  const handleNavigate = () => {
    navigation("/register");
  };

  return (
    <VStack spacing={4} maxW="400px" mx="auto" p={6}>
      <FormControl>
        <FormLabel>Username</FormLabel>
        <Input
          onChange={(e) => setUsername(e.target.value)}
          value={username}
          type="text"
        />
        <FormHelperText>Enter your username</FormHelperText>
      </FormControl>
      <FormControl>
        <FormLabel>Password</FormLabel>
        <Input
          onChange={(e) => setPassword(e.target.value)}
          value={password}
          type="password"
        />
        <FormHelperText>Enter your password</FormHelperText>
      </FormControl>
      <Button colorScheme="blue" onClick={handleLogin}>
        Login
      </Button>

      <Text onClick={handleNavigate} textDecoration={"underline"}>
        Don't have an account? Sing up!
      </Text>
    </VStack>
  );
};

export default Login;
