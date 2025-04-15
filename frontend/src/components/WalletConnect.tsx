import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

export default function WalletConnect() {
  return (
    <Card className="bg-slate-800 text-white">
      <CardContent className="p-4 space-y-4">
        <h2 className="text-xl font-semibold">Wallet Connection</h2>
        <p>No wallet connected yet.</p>
        <Button className="bg-emerald-600 hover:bg-emerald-700">Connect Wallet</Button>
      </CardContent>
    </Card>
  );
}
