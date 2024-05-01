import MessageContainer from "../../components/messages/MessageContainer";
import Sidebar from "../../components/sidebar/Sidebar";
import Marquee from "react-fast-marquee";
const Home = () => {
  return (
    // <div className='flex sm:h-[450px] md:h-[550px] rounded-lg overflow-hidden bg-gray-400 bg-clip-padding backdrop-filter backdrop-blur-lg bg-opacity-0'>
    // 	<Sidebar />
    // 	<MessageContainer />
    // </div>

    <div className="flex flex-col h-screen">
      <header className="bg-gray-800 text-white py-4 px-6">
        {/* Header content */}
        <Marquee className="text-xl font-semibold text-white">
          Chat-ify ~ A real time chat application.
        </Marquee>
        <h1 className="text-center text-white font-bold"></h1>
      </header>
      <main className="flex flex-1 overflow-hidden">
        <Sidebar />
        <MessageContainer />
      </main>
      <footer className="bg-gray-800 text-center text-white py-4 px-6">
        {/* Footer content */}
        <p>&copy; Created By Fazle Rabbi and team</p>
      </footer>
    </div>
  );
};
export default Home;
