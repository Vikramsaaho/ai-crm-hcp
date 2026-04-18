export default function Sidebar() {
  return (
    <div style={sidebar}>
      <h2>AI CRM</h2>
      <ul>
        <li>Dashboard</li>
        <li>HCP</li>
        <li>Analytics</li>
      </ul>
    </div>
  );
}

const sidebar = {
  width: "200px",
  height: "100vh",
  background: "#222",
  color: "#fff",
  padding: "20px"
};