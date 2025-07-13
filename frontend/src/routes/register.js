import {
  VStack,
  Button,
  FormControl,
  FormLabel,
  FormHelperText,
  Input,
  Select,
  useToast,
} from "@chakra-ui/react";

import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../contexts/useAuth";

const Register = () => {
  const [username, setUsername] = useState("");
  const [first_name, setFirstName] = useState("");
  const [surname, setSurname] = useState("");
  const [last_name, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [role, setRole] = useState("");
  const [password, setPassword] = useState("");
  const [passwordConfirm, setPasswordConfirm] = useState("");
  const [loading, setLoading] = useState(false);

  const navigation = useNavigate();
  const { register_user } = useAuth();
  const toast = useToast();

  const handleRegister = async () => {
    // Валидация
    if (
      !username ||
      !first_name ||
      !surname ||
      !last_name ||
      !email ||
      !role ||
      !password
    ) {
      toast({
        title: "Ошибка",
        description: "Пожалуйста, заполните все поля",
        status: "error",
        duration: 3000,
        isClosable: true,
      });
      return;
    }

    if (password !== passwordConfirm) {
      toast({
        title: "Ошибка",
        description: "Пароли не совпадают",
        status: "error",
        duration: 3000,
        isClosable: true,
      });
      return;
    }

    if (password.length < 6) {
      toast({
        title: "Ошибка",
        description: "Пароль должен содержать минимум 6 символов",
        status: "error",
        duration: 3000,
        isClosable: true,
      });
      return;
    }

    setLoading(true);
    try {
      await register_user(
        username,
        first_name,
        surname,
        last_name,
        email,
        role,
        password,
        passwordConfirm
      );
      toast({
        title: "Успешно",
        description: "Регистрация прошла успешно",
        status: "success",
        duration: 3000,
        isClosable: true,
      });
      navigation("/login");
    } catch (error) {
      toast({
        title: "Ошибка",
        description: "Ошибка при регистрации",
        status: "error",
        duration: 3000,
        isClosable: true,
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <VStack spacing={4} maxW="400px" mx="auto" p={6}>
      <FormControl isRequired>
        <FormLabel>Username</FormLabel>
        <Input
          onChange={(e) => setUsername(e.target.value)}
          value={username}
          type="text"
        />
        <FormHelperText>Enter your username</FormHelperText>
      </FormControl>

      <FormControl isRequired>
        <FormLabel>First name</FormLabel>
        <Input
          onChange={(e) => setFirstName(e.target.value)}
          value={first_name}
          type="text"
        />
        <FormHelperText>Enter your first name</FormHelperText>
      </FormControl>

      <FormControl isRequired>
        <FormLabel>Surname</FormLabel>
        <Input
          onChange={(e) => setSurname(e.target.value)}
          value={surname}
          type="text"
        />
        <FormHelperText>Enter your surname</FormHelperText>
      </FormControl>

      <FormControl isRequired>
        <FormLabel>Last name</FormLabel>
        <Input
          onChange={(e) => setLastName(e.target.value)}
          value={last_name}
          type="text"
        />
        <FormHelperText>Enter your last name</FormHelperText>
      </FormControl>

      <FormControl isRequired>
        <FormLabel>Email</FormLabel>
        <Input
          onChange={(e) => setEmail(e.target.value)}
          value={email}
          type="email"
        />
        <FormHelperText>Enter your email</FormHelperText>
      </FormControl>

      <FormControl isRequired>
        <FormLabel>Role</FormLabel>
        <Select
          placeholder="Выберите роль"
          onChange={(e) => setRole(e.target.value)}
          value={role}
        >
          <option value="doctor">Врач</option>
          <option value="dispatcher">Диспетчер</option>
        </Select>
        <FormHelperText>Выберите вашу должность</FormHelperText>
      </FormControl>

      <FormControl isRequired>
        <FormLabel>Password</FormLabel>
        <Input
          onChange={(e) => setPassword(e.target.value)}
          value={password}
          type="password"
        />
        <FormHelperText>
          Enter your password (минимум 6 символов)
        </FormHelperText>
      </FormControl>

      <FormControl isRequired>
        <FormLabel>Password Confirm</FormLabel>
        <Input
          onChange={(e) => setPasswordConfirm(e.target.value)}
          value={passwordConfirm}
          type="password"
        />
        <FormHelperText>Confirm password</FormHelperText>
      </FormControl>

      <Button
        onClick={handleRegister}
        colorScheme="blue"
        isLoading={loading}
        loadingText="Регистрация..."
        width="100%"
      >
        Register
      </Button>
    </VStack>
  );
};

export default Register;
