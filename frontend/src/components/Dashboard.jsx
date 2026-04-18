export default function Dashboard() {
  return (
    <div style={grid}>
      <div style={card}>Total Interactions</div>
      <div style={card}>Doctors Covered</div>
      <div style={card}>Positive Sentiment</div>
    </div>
  );
}

const grid = {
  display: "flex",
  gap: "20px",
  marginBottom: "20px"
};

const card = {
  padding: "20px",
  background: "#fff",
  borderRadius: "10px"
};