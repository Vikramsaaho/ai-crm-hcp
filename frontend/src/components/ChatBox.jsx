import { useState } from "react";
import API from "../services/api";

export default function ChatBox() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const sendMessage = async () => {
    const res = await API.post("/api/interact", { message });
    setResponse(res.data.response);
  };

  return (
    <div style={box}>
      <h3>AI Assistant</h3>

      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Enter message..."
      />

      <button onClick={sendMessage}>Send</button>

      <p>{response}</p>
    </div>
  );
}

const box = {
  padding: "20px",
  background: "#fff",
  borderRadius: "10px",
  marginBottom: "20px"
};
