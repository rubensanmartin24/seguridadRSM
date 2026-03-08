export default function DashboardPage() {
  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold">Resumen general</h2>

      <div className="grid md:grid-cols-3 gap-6">
        <div className="p-6 rounded-xl bg-slate-900/40 border border-slate-800">
          <p className="text-slate-400 text-sm">Alertas activas</p>
          <p className="text-3xl font-bold mt-2">0</p>
        </div>

        <div className="p-6 rounded-xl bg-slate-900/40 border border-slate-800">
          <p className="text-slate-400 text-sm">Eventos procesados</p>
          <p className="text-3xl font-bold mt-2">0</p>
        </div>

        <div className="p-6 rounded-xl bg-slate-900/40 border border-slate-800">
          <p className="text-slate-400 text-sm">Integraciones activas</p>
          <p className="text-3xl font-bold mt-2">0</p>
        </div>
      </div>
    </div>
  );
}
