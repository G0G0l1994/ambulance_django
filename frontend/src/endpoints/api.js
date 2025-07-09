import axios from "axios";

const baseUrl = "http://127.0.0.1:8000/api";
const loginUrl = `${baseUrl}/users/login/`;

export const login = async (username, password) => {
  const response = await axios.post(
    loginUrl,
    { username: username, password: password },
    { withCredentials: true }
  );
  return response.data.success;
};
