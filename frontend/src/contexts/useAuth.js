import { createContext, useContext, useEffect, useState } from "react";
import {
    is_autenticated,
    register,
    getProfile,
    getMyCrew,
} from "../endpoints/api";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [isAutenticated, setAuthenticated] = useState(false);
    const [loading, setLoading] = useState(true);
    const [profile, setProfile] = useState(null);
    const [myCrew, setMyCrew] = useState(null);

    const get_authenticated = async () => {
        try {
            const success = await is_autenticated();
            setAuthenticated(success);
            if (success) {
                const p = await getProfile();
                setProfile(p);
                const crew = await getMyCrew();
                setMyCrew(crew);
            } else {
                setProfile(null);
                setMyCrew(null);
            }
        } catch (error) {
            setAuthenticated(false);
            setProfile(null);
            setMyCrew(null);
        } finally {
            setLoading(false);
        }
    };

    const register_user = async (
        username,
        firstName,
        surname,
        lastName,
        email,
        role,
        password,
        passwordConfirm
    ) => {
        if (password === passwordConfirm) {
            try {
                await register(
                    username,
                    firstName,
                    surname,
                    lastName,
                    email,
                    role,
                    password,
                    passwordConfirm
                );
                return { success: true };
            } catch (error) {
                console.error("Registration error:", error);
                throw error;
            }
        } else {
            throw new Error("Password don't match");
        }
    };

    const refreshAuth = async () => {
        setLoading(true);
        await get_authenticated();
    };

    useEffect(() => {
        get_authenticated();
    }, []);

    return (
        <AuthContext.Provider
            value={{
                isAutenticated,
                loading,
                refreshAuth,
                register_user,
                profile,
                myCrew,
            }}
        >
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => useContext(AuthContext);
