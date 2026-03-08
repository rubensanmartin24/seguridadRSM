export default function TechSection() {
  const tech = [
    { name: "PostgreSQL", logo: "/postgresql.svg" },
    { name: "Redis", logo: "/redis.svg" },
    { name: "Grafana", logo: "/grafana.svg" },
    { name: "Loki", logo: "/loki.svg" },
    { name: "Sentry", logo: "/sentry.svg" },
  ];

  return (
    <section className="py-24">
      <div className="max-w-6xl mx-auto px-4 text-center">
        <h2 className="text-3xl md:text-4xl font-bold mb-12">
          Construido con tecnología moderna
        </h2>

        <p className="text-slate-400 max-w-2xl mx-auto mb-12">
          SecureMonitor se integra con herramientas líderes del sector para ofrecer
          monitorización, trazabilidad y seguridad en tiempo real.
        </p>

        <div className="grid grid-cols-2 md:grid-cols-5 gap-10 items-center justify-center">
          {tech.map((t, i) => (
            <div
              key={i}
              className="flex flex-col items-center opacity-70 hover:opacity-100 transition"
            >
              <img src={t.logo} alt={t.name} className="h-12 mb-3" />
              <span className="text-slate-300 text-sm">{t.name}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
