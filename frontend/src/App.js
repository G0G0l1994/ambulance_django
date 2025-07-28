// import axios from "axios";
import React from "react";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { ChakraProvider } from "@chakra-ui/react";

import Login from "./routes/login";
import CardsHistory from "./routes/history";
import CardPage from "./routes/card-create";
import MainPage from "./routes/main-page";
import MainLayout from "./components/MainLayout";
import DispatcherMain from "./routes/dispatcher-main";
import { AuthProvider } from "./contexts/useAuth";
import PrivateRoute from "./components/private_route";
import Register from "./routes/register";

function App() {
    return (
        <ChakraProvider>
            <Router>
                <AuthProvider>
                    <Routes>
                        <Route
                            path="/"
                            element={
                                <PrivateRoute>
                                    <MainLayout />
                                </PrivateRoute>
                            }
                        >
                            <Route path="/history" element={<CardsHistory />} />
                            <Route
                                path="/cards/create"
                                element={<CardPage />}
                            />
                            <Route
                                path="/dispatcher-main"
                                element={<DispatcherMain />}
                            />
                        </Route>

                        <Route path="/login" element={<Login />} />
                        <Route path="/register" element={<Register />} />
                    </Routes>
                </AuthProvider>
            </Router>
        </ChakraProvider>
    );
}

export default App;
