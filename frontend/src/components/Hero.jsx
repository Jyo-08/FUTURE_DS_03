function Hero({ kpis }) {
  return (
    <section className="mx-auto mt-8 max-w-7xl rounded-3xl bg-gradient-to-r from-blue-600 to-indigo-700 p-10 text-white shadow-xl">
      <p className="text-sm font-semibold uppercase tracking-[0.3em] text-blue-100">
        Growth Analytics
      </p>

      <h2 className="mt-4 text-5xl font-bold">
        Marketing Funnel Intelligence
      </h2>

      <p className="mt-5 max-w-3xl text-lg leading-8 text-blue-100">
        Analyze marketing funnel performance, identify conversion drop-offs,
        compare campaign effectiveness, and uncover growth opportunities using
        Python-powered analytics.
      </p>

      <div className="mt-10 grid grid-cols-2 gap-6 md:grid-cols-4">
        <Stat label="Total Contacts" value={kpis.total_contacts.toLocaleString()} />
        <Stat label="Converted" value={kpis.converted_customers.toLocaleString()} />
        <Stat label="Conversion Rate" value={`${kpis.conversion_rate}%`} />
        <Stat label="Drop-off Rate" value={`${kpis.dropoff_rate}%`} />
      </div>
    </section>
  );
}

function Stat({ label, value }) {
  return (
    <div className="rounded-2xl bg-white/10 p-6 backdrop-blur">
      <p className="text-sm text-blue-100">{label}</p>
      <h3 className="mt-2 text-4xl font-bold">{value}</h3>
    </div>
  );
}

export default Hero;