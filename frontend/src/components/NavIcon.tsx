export default function NavIcon({ icon, label, active, onClick }) {
  return (
    <button
      className={`flex flex-col items-center text-sm ${active ? 'text-emerald-400' : 'text-slate-400'}`}
      onClick={onClick}
    >
      {icon}
      <span>{label}</span>
    </button>
  );
}
