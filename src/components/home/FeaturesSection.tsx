import { Shield, Activity, Bell } from "lucide-react";

export default function FeaturesSection() {
  const features = [
    {
      title: "Detección en tiempo real",
      description:
        "Analiza eventos y comportamientos sospechosos al instante con nuestro motor de correlación.",
      icon: <Activity className="w-6 h-6 text-indigo-500" />,
    },
    {
      title: "Alertas inteligentes",
      description:
        "Recibe notificaciones precisas basadas en reglas avanzadas y machine learning.",
      icon: <Bell className="w-6 h-6 text-indigo-500" />,
    },
    {
      title: "Protección avanzada",
      description:
        "Identifica amenazas antes de que afecten a tu infraestructura con análisis predictivo.",
      icon: <Shield className="w-6 h-6 text-indigo-500" />,
    },
  ];

  return (
    <section className="py-24">
      <div className="max-w-6xl mx-auto px-4">
        <h2 className="text-3xl md:text-4xl font-bold text-center mb-12">
          Capacidades principales
        </h2>

        <div className="grid md:grid-cols-3 gap-10">
          {features.map((f, i) => (
            <div
              key={i}
              className="p-8 rounded-xl border border-slate-800 bg-slate-900/40 backdrop-blur-sm hover:bg-slate-900/60 transition"
            >
              <div className="mb-4">{f.icon}</div>
              <h3 className="text-xl font-semibold mb-2">{f.title}</h3>
              <p className="text-slate-400">{f.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
