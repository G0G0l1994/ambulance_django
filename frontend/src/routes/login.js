import {
  VStack,
  Button,
  FormControl,
  FormLabel,
  FormHelperText,
  Input,
} from "@chakra-ui/react";

import { useState } from "react";

import { login } from "../endpoints/api";

const Login = () => {

    const [username, setUsername] = useState('')
    const [password,setPassword] = useState('')

    const handleLogin = () => {
        login(username,password)

    }
  return (
    <VStack>
      <FormControl>
        <FormLabel>Username</FormLabel>
        <Input onChange={(e) => setUsername(e.target.value)} value={username} type="text" />
        <FormHelperText>Enter your username</FormHelperText>
      </FormControl>
      <FormControl>
        <FormLabel>Password</FormLabel>
        <Input onChange={(e) => setPassword(e.target.value)} value={password} type="password" />
        <FormHelperText>Enter your password</FormHelperText>
      </FormControl>
      <Button onClick={handleLogin}>Login</Button>
    </VStack>
  );
};

export default Login;
