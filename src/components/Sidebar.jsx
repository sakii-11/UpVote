import { NavLink } from "react-router-dom";
import PersonIcon from "@mui/icons-material/Person";
import Groups2OutlinedIcon from "@mui/icons-material/Groups2Outlined";
import LightbulbOutlinedIcon from "@mui/icons-material/LightbulbOutlined";


export default function Sidebar() {
  return (
    <div className="w-full h-full bg-black text-gray-300 p-4 space-y-4">
      <div className="space-y-2">
        <NavLink
          to="/home"
          className={({ isActive }) =>
            `flex items-center space-x-3 p-3 rounded-lg ${
              isActive ? "bg-gray-800 text-white" : ""
            }`
          }
        >
          <LightbulbOutlinedIcon />
          <span>Ideas</span>
        </NavLink>
        <NavLink
          to="/collaborate"
          className={({ isActive }) =>
            `flex items-center space-x-3 p-3 rounded-lg ${
              isActive ? "bg-gray-800 text-white" : ""
            }`
          }
        >
          <Groups2OutlinedIcon />
          <span>Collaborate</span>
        </NavLink>
        <NavLink
          to="/profile"
          className={({ isActive }) =>
            `flex items-center space-x-3 p-3 rounded-lg ${
              isActive ? "bg-gray-800 text-white" : ""
            }`
          }
        >
          <PersonIcon />
          <span>Profile</span>
        </NavLink>
      </div>
    </div>
  );
}
