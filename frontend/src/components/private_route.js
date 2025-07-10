import { Heading } from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";
import { useEffect } from "react";

import { useAuth } from "../contexts/useAuth";

const PrivateRoute = ({ children }) => {
  const { isAutenticated, loading } = useAuth();
  const navigate = useNavigate();

  console.log("PrivateRoute state:", { isAutenticated, loading });

  useEffect(() => {
    if (!loading && !isAutenticated) {
      console.log("Redirecting to login...");
      navigate("/login");
    }
  }, [isAutenticated, loading, navigate]);

  if (loading) {
    console.log("Showing loading...");
    return <Heading> Loading... </Heading>;
  }

  if (isAutenticated) {
    console.log("Showing protected content");
    return children;
  } else {
    console.log("Not authenticated, showing null");
    return null; // Не показываем ничего, пока идет редирект
  }
};

export default PrivateRoute;
