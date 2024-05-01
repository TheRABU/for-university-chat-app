import { Navigate, Route, Routes } from "react-router-dom";
import "./App.css";
import Home from "./pages/home/Home";
import Login from "./pages/login/Login";
import SignUp from "./pages/signup/SignUp";
import { Toaster } from "react-hot-toast";
import { useAuthContext } from "./context/AuthContext";
import LandingPage from "./pages/LandingPage";
import About from "./pages/About/About";

function App() {
  const { authUser } = useAuthContext();
  return (
    <div className="h-screen flex items-center justify-center flex-col">
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route
          path="/chat"
          element={authUser ? <Home /> : <Navigate to={"/login"} />}
        />
        <Route
          path="/login"
          element={authUser ? <Navigate to="/chat" /> : <Login />}
        />
        <Route
          path="/signup"
          element={authUser ? <Navigate to="/chat" /> : <SignUp />}
        />
        <Route path="/about-us" element={<About />} />
      </Routes>
      <Toaster />
    </div>
    // <div>
    //   <Routes>
    //     <Route path="/" element={<LandingPage />} />
    //     <Route
    //       path="/chat"
    //       element={authUser ? <Home /> : <Navigate to={"/login"} />}
    //     />
    //     <Route
    //       path="/login"
    //       element={authUser ? <Navigate to="/chat" /> : <Login />}
    //     />
    //     <Route
    //       path="/signup"
    //       element={authUser ? <Navigate to="/chat" /> : <SignUp />}
    //     />
    //   </Routes>
    //   <Toaster />
    // </div>
  );
}

export default App;
