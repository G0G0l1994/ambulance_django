import axios from "axios";

const BASE_URL = "/api";
const LOGIN_URL = `${BASE_URL}/users/login/`;
const CARDS_URL = `${BASE_URL}/cards/`;
const REFRESH_TOKEN = `${BASE_URL}/users/refresh/`;
const LOGOUT_URL = `${BASE_URL}/users/logout/`;
const AUTH_URL = `${BASE_URL}/authenticated/`;
const REGISTER_URL = `${BASE_URL}/registration/`;

export const login = async (username, password) => {
  const response = await axios.post(
    LOGIN_URL,
    { username: username, password: password },
    { withCredentials: true }
  );
  return response.data.success;
};

export const refreshToken = async () => {
  try {
    await axios.post(REFRESH_TOKEN, {}, { withCredentials: true });
    return true;
  } catch (error) {
    console.error("Refresh token failed:", error);
    return false;
  }
};

export const getCards = async () => {
  try {
    const response = await axios.get(CARDS_URL, { withCredentials: true });
    return response.data;
  } catch (error) {
    return callRefresh(error, () =>
      axios.get(CARDS_URL, { withCredentials: true })
    );
  }
};

const callRefresh = async (error, retryFunc) => {
  if (
    error.response &&
    (error.response.status === 401 || error.response.status === 403)
  ) {
    const tokenRefreshed = await refreshToken();

    if (tokenRefreshed) {
      try {
        const retryResponse = await retryFunc();
        return retryResponse.data;
      } catch (retryError) {
        console.error("Retry failed after refresh:", retryError);
        return false;
      }
    }
  }

  console.error("Request failed:", error);
  return false;
};

export const logout = async () => {
  try {
    await axios.post(LOGOUT_URL, {}, { withCredentials: true });
    return true;
  } catch (error) {
    return false;
  }
};

export const is_autenticated = async () => {
  try {
    const response = await axios.post(AUTH_URL, {}, { withCredentials: true });
    console.log("Auth API response:", response.data);
    return response.data.is_authenticated;
  } catch (error) {
    console.error("Auth check error:", error);
    return false;
  }
};

export const register = async (
  username,
  first_name,
  surname,
  last_name,
  email,
  role,
  password,
  passwordConfirm
) => {
  try {
    const requestData = {
      username: username,
      first_name: first_name,
      surname: surname,
      last_name: last_name,
      email: email,
      role: role,
      password: password,
      passwordConfirm: passwordConfirm,
    };

    console.log("Sending registration data:", requestData);

    const response = await axios.post(REGISTER_URL, requestData, {
      withCredentials: true,
    });

    console.log("Registration response:", response.data);
    return response.data;
  } catch (error) {
    console.error("Registration error:", error.response?.data || error.message);
    throw error;
  }
};
