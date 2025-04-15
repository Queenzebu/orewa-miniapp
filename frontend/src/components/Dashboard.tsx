import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

export default function Dashboard() {
  return (
    <Card className="bg-slate-800 text-white">
      <CardContent className="p-4 space-y-4">
        <h2 className="text-xl font-semibold">Welcome to OREWA!</h2>
        <p>🔹 OREVA Balance: 0.000</p>
        <p>🔹 ZIPP Balance: 0.000</p>
        <p>⛏️ Mining: Inactive</p>
        <p>📢 Notifications: None</p>
        <Button className="bg-emerald-600 hover:bg-emerald-700">Start Mining</Button>
      </CardContent>
    </Card>
  );
}
