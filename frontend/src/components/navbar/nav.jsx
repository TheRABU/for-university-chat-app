import { Link } from "react-router-dom";
const Nav = () => 
  {
  const links = (
    <>
      <li>
        <Link to="/">Home</Link>
      </li>
      <li>
        <Link to="/chat">Chat</Link>
      </li>
      <li>
        <Link to="/about-us">About Us</Link>
      </li>
      <li>
        <Link to="/signup">Register</Link>
      </li>
    </>
  );
  return (
    <div className="navbar bg-blue-100">
      <div className="navbar-start">
        <div className="dropdown">
          <div tabIndex={0} role="button" className="btn btn-ghost lg:hidden">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-5 w-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M4 6h16M4 12h8m-8 6h16"
              />
            </svg>
          </div>
          <ul
            tabIndex={0}
            className="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52"
          >
            {links}
          </ul>
        </div>
        <a className="btn btn-ghost text-xl">Chat-iFy</a>
      </div>
      <div className="navbar-center hidden lg:flex">
        <ul className="menu menu-horizontal px-1">{links}</ul>
      </div>
      <button className="btn btn-primary">
        <Link to="/chat">Chat Now</Link>
      </button>
    </div>
  );
};

export default Nav;
