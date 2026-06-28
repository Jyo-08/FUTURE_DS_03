function Navbar({ totalContacts, conversionRate }) {
  return (
    <nav className="sticky top-0 z-50 border-b border-slate-200 bg-white/90 backdrop-blur">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-8 py-4">
        <div>
          <h1 className="text-2xl font-bold text-slate-900">
            Marketing Funnel Intelligence
          </h1>
          <p className="text-sm text-slate-500">
            Executive Marketing Analytics Dashboard
          </p>
        </div>

        <div className="flex gap-6">
          <div className="text-center">
            <p className="text-xs uppercase tracking-wide text-slate-500">
              Contacts
            </p>
            <h2 className="text-xl font-bold text-blue-600">
              {totalContacts.toLocaleString()}
            </h2>
          </div>

          <div className="text-center">
            <p className="text-xs uppercase tracking-wide text-slate-500">
              Conversion
            </p>
            <h2 className="text-xl font-bold text-green-600">
              {conversionRate}%
            </h2>
          </div>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;