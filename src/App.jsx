import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Profile from "./pages/Profile";
import Collaborate from "./pages/Collaborate";
import Landing from "./pages/Landing";
import Signup from "./pages/Signup";
import PrivateRoute from "./components/PrivateRoute";
import Login from "./pages/Login";


function App() {
  return (
    <Routes>
      <Route path="/" element={<Landing />} />
      <Route path="/signup" element={<Signup />} />
      <Route path="/login" element={<Login />} />
      <Route element={<PrivateRoute />}>
        <Route path="/profile" element={<Profile />} />
        <Route path="/home" element={<Home />} />
        <Route path="/collaborate" element={<Collaborate />} />
      </Route>
    </Routes>
  );
}

export default App;
