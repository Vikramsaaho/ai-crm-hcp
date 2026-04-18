import Sidebar from "./components/Sidebar";
import Dashboard from "./components/Dashboard";
import ChatBox from "./components/ChatBox";
import InteractionTable from "./components/InteractionTable";

function App() {
  return (
    <div style={{ display: "flex" }}>
      <Sidebar />

      <div style={{ padding: "20px", flex: 1 }}>
        <h1>AI CRM Dashboard</h1>

        <Dashboard />
        <ChatBox />
        <InteractionTable />
      </div>
    </div>
  );
}

export default App;