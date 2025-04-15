import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

export default function Mining() {
  return (
    <Card className="bg-slate-800 text-white">
      <CardContent className="p-4 space-y-4">
        <h2 className="text-xl font-semibold">Mining Panel</h2>
        <p>Start mining and earn OREWA every day.</p>
        <Button className="bg-emerald-600 hover:bg-emerald-700">Start Mining</Button>
      </CardContent>
    </Card>
  );
}
