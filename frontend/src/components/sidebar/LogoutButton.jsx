import { BiLogOut } from "react-icons/bi";
import useLogout from "../../hooks/useLogout";

const LogoutButton = () => {
  const { loading, logout } = useLogout();

  return (
    <div className="mt-auto tooltip" data-tip="Logout Now">
      {!loading ? (
        <BiLogOut
          className="w-6 h-6 text-black cursor-pointer"
          onClick={logout}
        />
      ) : (
        <span className="loading loading-spinner"></span>
      )}
    </div>
    // 	<div className="tooltip" >
    // 	<button className="btn">Hover me</button>
    //   </div>
  );
};
export default LogoutButton;
