import video1 from "../assets/video1.mp4";
import video2 from "../assets/video2.mp4";

const HeroSection = () => {
  return (
    <div className="flex flex-col items-center mt-6 lg:mt-20">
      <h1 className="text-4xl sm:text-6xl lg:text-7xl text-center tracking-wide ">
        UpVote
        <span className="bg-gradient-to-r from-purple-500 to-red-800 text-transparent bg-clip-text">
          {" "}
          to Validate Ideas
        </span>
      </h1>
      <p className="mt-10 text-lg text-center text-neutral-500 max-w-4xl">
        Validate your ideas and find the right collaborators with Upvote! Share
        your vision, gain support through upvotes, and connect with like-minded
        innovators to bring your ideas to life. Start today and turn your
        concepts into reality!
      </p>
      <div className="flex justify-center my-10">
        <a
          href="/signup"
          className="bg-gradient-to-r from-purple-500 to-purple-800 py-3 px-4 mx-3 rounded-md"
        >
          Start
        </a>
      </div>
      <div className="flex mt-10 justify-center">
        <video
          autoPlay
          loop
          muted
          className="rounded-lg w-1/2 border border-purple-700 shadow-sm shadow-purple-400 mx-2 my-4"
        >
          <source src={video1} type="video/mp4" />
          Your browser does not support the video tag.
        </video>
        <video
          autoPlay
          loop
          muted
          className="rounded-lg w-1/2 border border-purple-700 shadow-sm shadow-purple-400 mx-2 my-4"
        >
          <source src={video2} type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </div>
    </div>
  );
};

export default HeroSection;
