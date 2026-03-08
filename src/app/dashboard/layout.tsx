import Header from "@/components/dashboard/Header";
import Sidebar from "@/components/dashboard/Sidebar";


export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex min-h-screen bg-slate-950 text-slate-100">
      <Sidebar />

      <div className="flex-1 flex flex-col">
        <Header />
        <main className="p-8 flex-1">{children}</main>
      </div>
    </div>
  );
}
