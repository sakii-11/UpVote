import { Box, Button, Typography } from "@mui/material";
import { Link } from "react-router-dom";

export default function Landing() {
  return (
    <Box
      sx={{
        height: "100vh",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "#000",
        color: "#fff",
        textAlign: "center",
      }}
    >
      <Typography variant="h3" fontWeight="bold" gutterBottom>
        UpVote
      </Typography>


      <Typography variant="h6" color="gray" mb={4}>
        Validate Your Ideas. Find Collaborators.
      </Typography>


      <Box display="flex" gap={3}>
        <Link to="/login" style={{ textDecoration: "none" }}>
          <Button
            variant="contained"
            sx={{
              backgroundColor: "#000",
              color: "#fff",
              border: "2px solid white",
              transition: "all 0.3s",
              "&:hover": {
                boxShadow: "0px 0px 15px white",
                backgroundColor: "#111",
              },
            }}
          >
            Login
          </Button>
        </Link>

        <Link to="/signup" style={{ textDecoration: "none" }}>
          <Button
            variant="contained"
            sx={{
              backgroundColor: "#000",
              color: "#fff",
              border: "2px solid white",
              transition: "all 0.3s",
              "&:hover": {
                boxShadow: "0px 0px 15px white",
                backgroundColor: "#111",
              },
            }}
          >
            Sign Up
          </Button>
        </Link>
      </Box>
    </Box>
  );
}
