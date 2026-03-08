export default function Hero() {
  return (
    <section className="min-h-[calc(100vh-4rem)] flex items-center">
      <div className="grid md:grid-cols-2 gap-12 items-center w-full">

        {/* Texto */}
        <div className="space-y-6">
          <h1 className="text-4xl md:text-5xl font-bold leading-tight">
            Monitoriza, detecta y responde a amenazas en tiempo real.
          </h1>

          <p className="text-slate-400 text-lg">
            SecureMonitor es una plataforma moderna de observabilidad y seguridad
            diseñada para equipos que necesitan control total sobre su infraestructura.
          </p>

          <div className="flex gap-4">
            <a
              href="/auth/register"
              className="px-6 py-3 rounded-md bg-indigo-600 hover:bg-indigo-700 text-white transition"
            >
              Empezar gratis
            </a>

            <a
              href="#"
              className="px-6 py-3 rounded-md border border-slate-700 hover:bg-slate-800 transition"
            >
              Ver demo
            </a>
          </div>

          <p className="text-slate-500 text-sm">
            Sin tarjeta de crédito. Pensado para equipos de seguridad.
          </p>
        </div>

        {/* Panel visual */}
        <div className="hidden md:block">
          <div className="w-full h-80 rounded-xl border border-slate-800 bg-slate-900/40 backdrop-blur-sm p-6 flex items-center justify-center">
            <div className="text-slate-500 text-center">
              Panel visual<br /> (aquí luego añadiremos gráficos o animaciones)
            </div>
          </div>
        </div>

      </div>
    </section>
  );
}
