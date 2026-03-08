export default function CTASection() {
  return (
    <section className="py-32">
      <div className="max-w-4xl mx-auto px-6 text-center">
        
        <div className="p-12 rounded-2xl bg-gradient-to-br from-indigo-600/20 via-indigo-500/10 to-slate-900 border border-indigo-600/30 shadow-xl backdrop-blur-md">
          
          <h2 className="text-3xl md:text-4xl font-bold mb-6">
            Empieza a proteger tu infraestructura hoy mismo
          </h2>

          <p className="text-slate-300 text-lg mb-10 max-w-2xl mx-auto">
            SecureMonitor te ofrece monitorización, alertas inteligentes y análisis en tiempo real.
            Diseñado para equipos que necesitan seguridad sin complicaciones.
          </p>

          <a
            href="/auth/register"
            className="px-8 py-4 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white text-lg transition shadow-lg"
          >
            Crear cuenta gratuita
          </a>

          <p className="text-slate-500 text-sm mt-6">
            Sin tarjeta de crédito. Cancela cuando quieras.
          </p>
        </div>

      </div>
    </section>
  );
}
