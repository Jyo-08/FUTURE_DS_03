import useAnalytics from "./hooks/useAnalytics";
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";

function App() {
  const { data, loading, error } = useAnalytics();

  if (loading) return <h1 className="p-10 text-3xl">Loading...</h1>;
  if (error) return <h1 className="p-10 text-red-600">{error}</h1>;

  return (
  <div className="min-h-screen bg-slate-100">
    <Navbar
      totalContacts={data.kpis.total_contacts}
      conversionRate={data.kpis.conversion_rate}
    />

    <Hero kpis={data.kpis} />
  </div>
);
}

export default App;