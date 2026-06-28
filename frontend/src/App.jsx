import useAnalytics from "./hooks/useAnalytics";

function App() {
  const { data, loading, error } = useAnalytics();

  if (loading) return <h1 className="p-10 text-3xl">Loading...</h1>;
  if (error) return <h1 className="p-10 text-red-600">{error}</h1>;

  return (
    <div className="min-h-screen bg-slate-100 p-10">
      <div className="rounded-3xl bg-white p-8 shadow-xl">
        <h1 className="text-4xl font-bold text-slate-900">
          Marketing Funnel Intelligence
        </h1>

        <p className="mt-3 text-slate-500">
          React connected to Python analytics JSON.
        </p>

        <h2 className="mt-8 text-6xl font-bold text-blue-600">
          {data.kpis.total_contacts}
        </h2>

        <p className="mt-2 text-slate-500">Total Contacts</p>
      </div>
    </div>
  );
}

export default App;