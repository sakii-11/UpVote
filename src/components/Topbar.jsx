import PropTypes from "prop-types";
import logo from "../assets/logo.png";

const Topbar = ({ title }) => {
  return (
    <div className="flex items-center text-white p-4 shadow-md">
      <div className="flex items-center space-x-2">
        <img
          src={logo}
          alt="logo"
          width={30} 
          height={30} 
          className="rounded-lg shadow-lg "
        />
        <span className="text-2xl font-bold font-garamond">UpVote</span>
      </div>

      {/* Dynamic Title */}
      <h1 className="absolute left-1/2 transform -translate-x-1/2 text-2xl font-medium font-garamond">
        {title}
      </h1>
    </div>
  );
};

Topbar.propTypes = {
  title: PropTypes.string.isRequired, 
};

export default Topbar;
