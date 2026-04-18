import { useEffect, useState } from "react";
import API from "../services/api";

export default function InteractionTable() {
  const [data, setData] = useState([]);

  useEffect(() => {
    API.get("/api/history")
      .then(res => setData(res.data))
      .catch(() => {});
  }, []);

  return (
    <div style={box}>
      <h3>Interactions</h3>

      <table width="100%" border="1">
        <thead>
          <tr>
            <th>Doctor</th>
            <th>Message</th>
            <th>Sentiment</th>
          </tr>
        </thead>

        <tbody>
          {data.map((item, i) => (
            <tr key={i}>
              <td>{item.hcp_name}</td>
              <td>{item.message}</td>
              <td>{item.sentiment}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

const box = {
  padding: "20px",
  background: "#fff",
  borderRadius: "10px"
};