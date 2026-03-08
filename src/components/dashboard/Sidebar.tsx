import Link from "next/link";
import { LayoutDashboard, Bell, Shield, Settings } from "lucide-react";

export default function Sidebar() {
  const items = [
    { label: "Dashboard", href: "/dashboard", icon: <LayoutDashboard className="w-5 h-5" /> },
    { label: "Alertas", href: "/dashboard/alertas", icon: <Bell className="w-5 h-5" /> },
    { label: "Eventos", href: "/dashboard/eventos", icon: <Shield className="w-5 h-5" /> },
    { label: "Integraciones", href: "/dashboard/integraciones", icon: <Settings className="w-5 h-5" /> },
    { label: "Configuración", href: "/dashboard/configuracion", icon: <Settings className="w-5 h-5" /> },
  ];

  return (
    <aside className="w-64 h-screen bg-slate-950 border-r border-slate-800 p-6 flex flex-col">
      <div className="text-2xl font-bold mb-10">
        Secure<span className="text-indigo-500">Monitor</span>
      </div>

      <nav className="flex-1 space-y-4">
        {items.map((item, i) => (
          <Link
            key={i}
            href={item.href}
            className="w-full flex items-center gap-3 px-3 py-2 rounded-lg text-slate-300 hover:bg-slate-800 hover:text-white transition"
          >
            {item.icon}
            {item.label}
          </Link>
        ))}
      </nav>
    </aside>
  );
}
