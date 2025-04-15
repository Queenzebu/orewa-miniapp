import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

export default function Profile() {
  return (
    <Card className="bg-slate-800 text-white">
      <CardContent className="p-4 space-y-4">
        <h2 className="text-xl font-semibold">Your Profile</h2>
        <p>Username: @telegram_user</p>
        <p>Status: Vanguard Member</p>
        <Button className="bg-emerald-600 hover:bg-emerald-700">Edit Profile</Button>
      </CardContent>
    </Card>
  );
}
