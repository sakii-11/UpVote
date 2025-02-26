import Filter from "../components/Filter";
import PostList from "../components/PostList";
import Sidebar from "../components/Sidebar";
import Topbar from "../components/topbar";


export default function Home() {
  return (
    <div className="h-screen flex flex-col bg-black text-white">
      <div className="w-full border-b shadow-md">
        <Topbar title="Collaborate" />
      </div>

      <div className="flex flex-1 shadow-lg">

        <div className="w-1/4 md:w-1/6 p-4 border-r ">
          <Sidebar />
        </div>


        <div className="w-1/2 md:w-2/3 p-4 border-r ">
          <PostList />
        </div>

        <div className="w-1/4 md:w-1/6 p-4">
          <Filter />
        </div>
      </div>
    </div>
  );
}
