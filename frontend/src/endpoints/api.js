import axios from "axios";

const BASE_URL = "/api";
const LOGIN_URL = `${BASE_URL}/users/login/`;
const CARDS_URL = `${BASE_URL}/cards/`;
const CARD_CREATE_URL = `${BASE_URL}/cards/create/`;
const REFRESH_TOKEN = `${BASE_URL}/users/refresh/`;
const LOGOUT_URL = `${BASE_URL}/users/logout/`;
const AUTH_URL = `${BASE_URL}/authenticated/`;
const REGISTER_URL = `${BASE_URL}/registration/`;
const PROFILE_URL = `${BASE_URL}/users/profile/`;
const MKB_URL = `${BASE_URL}/mkb/`;
const ONLINE_DOCTORS = `${BASE_URL}/users/doctor-list/`;
const CREW_LIST = `${BASE_URL}/crew/list/`;
const DOCTORS_LIST = `${BASE_URL}/users/`;
// Получение бригады текущего пользователя без изменений бэкенда
// Делается на клиенте через профиль + список бригад

export const login = async (username, password) => {
    const response = await axios.post(
        LOGIN_URL,
        { username: username, password: password },
        { withCredentials: true }
    );
    return response.data;
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

export const getDoctorsList = async () => {
    try {
        const response = await axios.get(DOCTORS_LIST, {
            withCredentials: true,
        });
        console.log(response.data);
        return response.data;
    } catch (error) {
        return callRefresh(error, () => {
            return axios.get(DOCTORS_LIST, { withCredentials: true });
        });
    }
};

export const getCardsList = async () => {
    try {
        const response = await axios.get(CARDS_URL, { withCredentials: true });
        return response.data;
    } catch (error) {
        return callRefresh(error, () => {
            return axios.get(CARDS_URL, { withCredentials: true });
        });
    }
};

export const getCardsDoctorList = async (user_id) => {
    try {
        const response = await axios.get(`${CARDS_URL}doctor/${user_id}`, {
            withCredentials: true,
        });
        return response.data;
    } catch (error) {
        return callRefresh(error, () => {
            return axios.get(CARDS_URL, { withCredentials: true });
        });
    }
};

export const getCard = async (card_id) => {
    try {
        const response = await axios.get(`${CARDS_URL}${card_id}/`, {
            withCredentials: true,
        });
        return response.data;
    } catch (error) {
        return callRefresh(error, () => {
            return axios.get(`${CARDS_URL}${card_id}/`, {
                withCredentials: true,
            });
        });
    }
};

export const getMKB = async () => {
    try {
        const response = await axios.get(`${MKB_URL}`, {
            withCredentials: true,
        });
        return response.data;
    } catch (error) {
        return await axios.get(`${MKB_URL}`, { withCredentials: true });
    }
};

export const patchCard = async (card_id, update_data) => {
    try {
        const response = await axios.put(
            `${CARDS_URL}${card_id}/update/`,
            update_data,
            {
                withCredentials: true,
            }
        );
        return response.data;
    } catch (error) {
        return callRefresh(error, () => {
            return axios.put(`${CARDS_URL}${card_id}/update/`, update_data, {
                withCredentials: true,
            });
        });
    }
};

export const getCrewList = async () => {
    try {
        const response = await axios.get(CREW_LIST, { withCredentials: true });
        return response.data;
    } catch (error) {
        return callRefresh(error, () => {
            return axios.get(CREW_LIST, { withCredentials: true });
        });
    }
};

export const updateCrew = async (crew_id, update_data) => {
    try {
        const response = await axios.put(
            BASE_URL + `/crew/${crew_id}/update/`,
            update_data,
            { withCredentials: true }
        );
        return response.data;
    } catch (error) {
        return callRefresh(error, () => {
            return axios.put(BASE_URL + `/${crew_id}/update`, update_data, {
                withCredentials: true,
            });
        });
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
                throw retryError;
            }
        }
    }
    throw error;
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
        const response = await axios.post(
            AUTH_URL,
            {},
            { withCredentials: true }
        );
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

        const response = await axios.post(REGISTER_URL, requestData, {
            withCredentials: true,
        });

        return response.data;
    } catch (error) {
        throw error;
    }
};

export const getProfile = async () => {
    try {
        const profile = await axios.get(PROFILE_URL, { withCredentials: true });
        return profile.data;
    } catch (error) {
        return callRefresh(error, () => {
            axios.get(PROFILE_URL, { withCredentials: true });
        });
    }
};

export const getMyCrew = async () => {
    try {
        const [profile, crews] = await Promise.all([
            getProfile(),
            getCrewList(),
        ]);
        if (!profile || !Array.isArray(crews)) return null;
        const mine = crews.find(
            (c) => c.main === profile.id || c.secondary === profile.id
        );
        return mine || null;
    } catch (error) {
        return null;
    }
};

export const cardCreate = async (formData) => {
    try {
        const response = await axios.post(CARD_CREATE_URL, formData, {
            withCredentials: true,
        });
        return response.data;
    } catch (error) {
        throw error;
    }
};

export const getOnlineDoctors = async () => {
    try {
        const response = await axios.get(ONLINE_DOCTORS, {
            withCredentials: true,
        });
        return response.data;
    } catch (error) {
        return callRefresh(error, () => {
            axios.get(ONLINE_DOCTORS, { withCredentials: true });
        });
    }
};
